# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import urllib.request
import re
from fake_useragent import UserAgent
import chardet
import requests
from jdbooks.items import JdbooksItem

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["jd.com"]
    # start_urls = ['http://jd.com/']
    def start_requests(self):
        try:
            ua = UserAgent()
            header = ua.random
            headers = {"User-Agent":header}
        except Exception as e:
            pass
        # req = urllib.request.Request("https://book.jd.com/")
        # req.add_header("User-Agent",headers)
        # response = urllib.request.urlopen(req).read()
        # data = response.decode(chardet.detect(response["encoding"]),"ignore")
        requests.packages.urllib3.disable_warnings()
        response = requests.get("https://book.jd.com/",headers=headers,verify=False)
        data = bytes(response.text,response.encoding).decode("gbk","ignore")
        reg1 = '"URL":"\\\\/\\\\/(channel.jd.com\\\\/.*?.html)"'
        #得到所有的图书分类链接
        alla = re.compile(reg1,re.S).findall(data)
        catall = []
        for i in alla:
            thispd = "http://"+i.replace("\\","")
            # print(thispd)
            requests.packages.urllib3.disable_warnings()
            response2 = requests.get(thispd,headers=headers,verify=False)
            pddata = bytes(response2.text,response2.encoding).decode("gbk","ignore")
            reg2 = 'href="..list.jd.com.list.html.cat=([0-9,]*?)[&"]'
            #得到所有的书籍的cat
            cat = re.compile(reg2,re.S).findall(pddata)
            for j in cat:
                catall.append(j)
            #去重
        catall2 = set(catall)
        # print("---------------->"+str(catall2))
        #进入每个书籍类型的所有书籍的网页，并得到所有的数据
        #k为每个网页的cat
        flag = 0 #标志位
        allcat = []
        for k in catall2:
            thispdnum = k
            url = "https://list.jd.com/list.html?cat="+thispdnum
            #去除警告
            requests.packages.urllib3.disable_warnings()
            response3 = requests.get(url=url,headers=headers,verify=False)
            pddata2 = bytes(response3.text,response3.encoding).decode("utf-8","ignore")
            reg3 = '<em>共<b>(.*?)</b>'
            #得到所有的页数
            allpage = re.compile(reg3,re.S).findall(pddata2)
            # print(allpage)
            if len(allpage)>0:
                # allpage = allpage[0]
                pass
            else:
                allpage = [1] #若没有值则让其只爬取第1页



            #m为页数，构造一个一个字典，一个cat对应一个页数

            allcat.append({thispdnum:allpage[0]})

            # print(allcat)
            if flag > 2:
                break
            flag += 1

            # 构造出每页的地址
        x = 0
        for n in catall2:
            #从字典中得到页数
            thispage = allcat[x][n]
            for p in range(1,int(thispage) + 1):
                thispageurl = "https://list.jd.com/list.html?cat="+ str(n) +"&page="+str(p)
                # print(thispageurl)
                yield Request(thispageurl,callback=self.parse)
            x += 1

    def parse(self, response):
        # print("ssssssssss")
        item = JdbooksItem()
        listdata = response.body.decode("utf-8","ignore")
        # print(listdata)

        #频道号
        pd = response.xpath("//span[@class='curr']/text()").extract()
        # print(pd)
        if len(pd) == 0:
            pd = ["缺省","缺省"]
        if len(pd) == 1:
            pda = pd[0]
            pd = [pda,"缺省"]
        pd1 = pd[0]
        pd2 = pd[1]
        # print(pd1)

        allskupat = '<a data-sku="(.*?)"'
        allsku = re.compile(allskupat, re.S).findall(listdata)
        # print(allsku)
        #图书名
        bookname = response.xpath("//div[@class='p-name']/a/em/text()").extract()
        # print(bookname)
        #作者
        author = response.xpath("//span[@class='author_type_1']/a/text()").extract()
        #出版社
        pub = response.xpath("//span[@class='p-bi-store']/a/text()").extract()
        #店铺名
        seller = response.xpath("//div[@class='p-shopnum']/span/text()").extract()
        # print(seller)
        for i in range(0,len(seller)):
            thisbookname = bookname[i+3]
            # print(thisbookname)
            thisauthor = author[i]
            thispub = pub[i]
            thisseller = seller[i]
            sku = allsku[i]
            # print(sku)
            #价格
            priceurl = "https://p.3.cn/prices/mgets?callback=jQuery7486873&ext=11101000&pin=&type=1&area=1_72_4137_0&skuIds=J_"+str(sku)
            pricedata = urllib.request.urlopen(priceurl).read().decode("utf-8","ignore")
            pricepat = '"p":"(.*?)"}'
            thisprice = re.compile(pricepat,re.S).findall(pricedata)[0]
            # print(thisprice)
            #评论数
            commenturl = "https://club.jd.com/comment/productCommentSummaries.action?my=pinglun&referenceIds="+str(sku)
            commentdata = urllib.request.urlopen(commenturl).read().decode("utf-8","ignore")
            commentpat = '"CommentCount":(.*?),'
            thiscomment = re.compile(commentpat,re.S).findall(commentdata)[0]
            #测试
            '''
            print(thisbookname)
            print(thisauthor)
            print(thispub)
            print(thisseller)
            print(thisprice)
            print(thiscomment)
            '''
            item["pd1"] = pd1
            item["pd2"] = pd2
            item["name"] = thisbookname
            item["author"] = thisauthor
            item["pub"] = thispub
            item["price"] = thisprice
            item["cnum"] = thiscomment
            item["seller"] = thisseller
            yield item




        # item["pdnum"]