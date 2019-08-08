# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
class HexuntestPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host="127.0.0.1",user="root",passwd="fuck580",db="mydb")
    def process_item(self, item, spider):
        title = item["title"][0]
        link = item["link"]
        click = item["click"]
        comment = item["comment"]
        sql = "insert into hexuntest(title,link,click,comment) values ('"+str(title)+"','"+str(link)+"','"+str(click)+"','"+str(comment)+"')"
        self.conn.query(sql)
        self.conn.commit()
        return item
    def close_spider(self,spider):
        self.conn.close()
