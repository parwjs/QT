# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from hexun.items import HexunItem
import re
import urllib.request
class HxSpider(CrawlSpider):
    name = 'hx'
    allowed_domains = ['hexun.com']
    start_urls = ['http://blog.hexun.com/']

    rules = (
        Rule(LinkExtractor(allow=('http://.*?.blog.hexun.com/.*?_d.html'),allow_domains=('hexun.com')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = HexunItem()
        item["title"] = response.xpath("//span[@class='ArticleTitleText']/a/text()").extract()
        item["link"] = response.url
        pat_link = '(http://click.tool.hexun.com/click.aspx\?articleid=.*?)"'
        click_link = re.compile(pat_link,re.S).findall(str(response.body))[0]
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
            'Referer': response.url
        }
        opener = urllib.request.build_opener()
        headall = []
        for key, value in headers.items():
            headers_item = (key, value)
            headall.append(headers_item)
        opener.addheaders = headall
        urllib.request.install_opener(opener)
        click_data = urllib.request.urlopen(click_link).read().decode("utf-8",'ignore')
        pat_click = '"articleClickCount"\).innerHTML = (.*?);'
        pat_comment = '"articleCommentCount"\).innerHTML = (.*?);'
        click = re.compile(pat_click,re.S).findall(click_data)[0]
        commemt = re.compile(pat_comment,re.S).findall(click_data)[0]
        print(click,commemt)
        item["click"] = click
        item["comment"] = commemt
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return item
