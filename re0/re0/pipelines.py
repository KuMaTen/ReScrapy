# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import json

class Re0Pipeline(object):
  def __init__(self):
    self.f = open("title.txt", "w",encoding="utf-8")
    pass
  
  def process_item(self, item, spider):
    self.f = open(item['chapTitle']+".txt", "w", encoding="utf-8")
    self.f.write(item['chapTitle']+'\n')
    self.f.write(item['chapInfo']+'\n')
    self.f.close()
    return item
  
  def close_spider(self, spider):
    self.f.close()
    pass
