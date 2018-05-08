# -*- coding: utf-8 -*-
import scrapy
from re0.items import Re0Item
import time


class Re0Spider(scrapy.Spider):
  name = 'Re0'
  allowed_domains = ['http://ncode.syosetu.com']
  
  base_url = 'http://ncode.syosetu.com'
  init_url = '/n2267be/1/'
  
  # start_urls = [base_url+init_url]
  start_urls = ['http://ncode.syosetu.com/n2267be/1/']
  
  # first http://ncode.syosetu.com/n2267be/1/#main
  #name //div[@class='index_box']/dl[@class='novel_sublist2']/dd[@class='subtitle']/a/text()
  #href //div[@class='index_box']/dl[@class='novel_sublist2']/dd[@class='subtitle']/a/@href
  #title  //div[@id='novel_color']/p[@class='novel_subtitle']/text()  -->标题
  #info //div[@id='novel_color']/div[@id='novel_honbun']/text()  -->正文

  # 所有界面内容获取
  def parse(self, response):
    node_list = response.xpath("//div[@id='novel_color']")
    
    for node in node_list:
      item = Re0Item()
      item['chapTitle'] = node.xpath("./p[@class='novel_subtitle']/text()").extract()[0]
      tempItem = node.xpath("./div[@id='novel_honbun']/text()").extract()
      
      # for tempI in tempItem:
      #   item['chapInfo'] = tempI
      #   time.sleep(0.1)
      tempStr = ""
      for tempI in tempItem:
        tempStr = tempStr + tempI
        
      # print(tempStr)
      # tempStr = tempStr.replace("\u3000","")
      # tempStr = tempStr.replace("\n","")
      item['chapInfo'] = tempStr
      yield item
      
      tempNext = node_list.xpath("./div[@class='novel_bn']/a/text()").extract()
      for tempN in tempNext:
        if tempN == '次へ >>':
          yield item
        else:
          continue
          
    
    # if len(node_list.xpath("./div[@class='novel_bn']/a"))==2:
    #   url = node_list.xpath("./div[@class='movel_bn']/a[2]").extract()[0]
    #   yield scrapy.Request("http://nocode.syosetu.com" + url, callback=self.parse)
    # item['chapInfo']
    # yield item
    
























    # 单个界面
    # def parse(self, response):
    #   node_list = response.xpath("//div[@class='index_box']/dl[@class='novel_sublist2']/dd[@class='subtitle']/a")
    #
    #   for node in node_list:
    #     item =Re0Item()
    #     item['chapname'] = node.xpath("./text()").extract()[0]
    #     item['chapURL'] = node.xpath("./@href").extract()[0]
    #     # item['chapInfo']
    #     yield item
    #   pass
