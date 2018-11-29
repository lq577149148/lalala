# -*- coding: utf-8 -*-
import scrapy,re
import win_unicode_console
win_unicode_console.enable()


class XinlangwSpider(scrapy.Spider):
    name = 'xinlangw'
    # allowed_domains = ['https://tech.sina.com.cn/']
    # start_urls = ['http://https://tech.sina.com.cn//']
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
    }

    def start_requests(self):
        url = 'https://cre.mix.sina.com.cn/api/v3/get?callback=jQuery111207968306441067055_1543491108967&cateid=1z&cre=tianyi&mod=pctech&merge=3&statics=1&length=15&up=11&down=0&tm=1543491123&action=1&top_id=%2CA1u1J%2CA1rkN%2CA1s5b%2CA1mJl%2CA1PbX%2CA1MSP%2CA1fbh%2CA1Rzi%2CA1MWO%2CA1MEd%2C%2C9Eux1%2C%2C&offset=0&ad=%7B%22rotate_count%22%3A100%2C%22platform%22%3A%22pc%22%2C%22channel%22%3A%22tianyi_pctech%22%2C%22page_url%22%3A%22https%3A%2F%2Ftech.sina.com.cn%2F%22%2C%22timestamp%22%3A1543491109033%7D&ctime=1543370711&_=1543491108980'
        yield scrapy.Request(url=url,callback=self.parse,headers=self.header)

    def parse(self, response):
        link = re.findall('"url_https":"(.*?)"',response.text)
        print(link,'===========================')
        for i in link:
            urls = eval(repr(i).replace('\\',''))
            print(urls)
            yield scrapy.Request(url=urls,callback=self.parse_1,headers=self.header)

    def parse_1(self, response):
        if re.findall('<title>(.*?)</title>',response.text):
            title = re.findall('<title>(.*?)</title>',response.text)
            print(title)
        else:
            title = "没有标题"
            print(title)

        if response.xpath("//div[@class='article-content-left']/div[@id='artibody']/p[2]/text()").extract():
            daodu = response.xpath("//div[@class='article-content-left']/div[@id='artibody']/p[2]/text()").extract()
            print(daodu)
        else:
            daodu = "没有导读"
            print(daodu)

        if response.xpath("//div[@class='article-content-left']/div[@id='artibody']/p/text()").extract():
            neirong = response.xpath("//div[@class='article-content-left']/div[@id='artibody']/p/text()").extract()
            print(neirong)
        else:
            neirong = "没有内容"
            print(neirong)

        if response.xpath("//div[@class='article-content-left']/div[@id='artibody']/p[1]/text()").extract():
            zuozhe = response.xpath("//div[@class='article-content-left']/div[@id='artibody']/p[1]/text()").extract()
            print(zuozhe)

        else:
            zuozhe = "没有作者"
            print(zuozhe)

        if response.xpath("//div[@class='date-source']/span[@class='date']/text()").extract():
            data_time = response.xpath("//div[@class='date-source']/span[@class='date']/text()").extract()
            print(data_time)
        else:
            data_time = "没有时间"
            print(data_time)

        if response.xpath("//div[@id='article-bottom']/div[@id='keywords']/a/text()").extract():
            ganjian = response.xpath("//div[@id='article-bottom']/div[@id='keywords']/a/text()").extract()
            print(ganjian)

        else:
            ganjian = "没有关键字"
            print(ganjian)