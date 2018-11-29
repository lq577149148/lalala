# -*- coding: utf-8 -*-
import scrapy,re,rules,time
import win_unicode_console
win_unicode_console.enable()
from scrapy.selector import Selector
from scrapy.spiders import Rule,CrawlSpider
from scrapy.linkextractors import LinkExtractor



class RengongwSpider(scrapy.Spider):
    name = 'rengongw'
    # allowed_domains = ['http://ai.ailab.cn/?page=2']
    start_urls = ['http://ai.ailab.cn/?page=2/']
    time.sleep(3)
    # rules = (
    #     Rule(LinkExtractor(allow='http://ai.ailab.cn/?page=2'),follow=True),
    #     Rule(LinkExtractor(allow='http://ai.ailab.cn/article-(.*?).html'),follow=False,callback='parse_item'),
    # )


    def parse(self, response):
        print(response.text,'===================')
        a = re.findall('http://ai.ailab.cn/article-(.*?).html',response.text)
        print(a)
