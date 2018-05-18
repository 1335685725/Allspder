# -*- coding: utf-8 -*-
import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    # allowed_domains = ['python123.io'] 不需要
    start_urls = ['http://python123.io/ws/demo.html']

    def parse(self, response):
        fame = response.url.split('/')[-1]
        with open(fame,"wb") as f:
            f.write(response.body)
        self.log("Saved file %s".format(DemoSpider.name))
        pass

    def start_requests(self):
        pass