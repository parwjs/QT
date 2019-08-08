# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request,FormRequest
import json
class DbSpider(scrapy.Spider):
    name = "db"
    allowed_domains = ["douban.com"]
    header = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        'Referer': 'https://accounts.douban.com/passport/login_popup?login_source=anony'
    }
    # start_urls = ['http://douban.com/']
    def start_requests(self):
        #首先爬一次登录界面，然后进入回调函数parse()
        return [Request("https://www.douban.com/",meta={"cookiejar":1},callback=self.parse)]

    def parse(self, response):
        data = {
            'ck':'',
            'name':'13359504512',
            'password':'perwjs99509...',
            'remember':'false',
            'ticket':''
        }
        print("登录中...")
        return [FormRequest.from_response(response,
                                          method='POST',
                                          url="https://accounts.douban.com/j/mobile/login/basic",
                                          #设置cookie信息
                                          meta={"cookiejar":response.meta["cookiejar"]},
                                          #设置headers信息模拟成浏览器
                                          headers=self.header,
                                          #设置post表单中的数据
                                          formdata=data,
                                          #设置回调函数
                                          callback=self.next,
        )]

    def next(self,response):
        return [Request(url="https://www.douban.com/people/190461018/",meta={"cookiejar":response.meta["cookiejar"]},callback=self.userindex)]

    def userindex(self,response):
        title = response.xpath("/html/head/title/text()").extract()
        print("---------------"+str(title))






