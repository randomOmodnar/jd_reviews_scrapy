# -*- coding: utf-8 -*-
import scrapy
import logging
import datetime
import random, time, requests, json


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']

    def __init__(self, keyword, *args, **kwargs):
        super(JdSpider, self).__init__(*args, **kwargs)
        # super().__init__(**kwargs)
        self.start_url = 'https://search.jd.com/Search?keyword={}'.format(keyword)

    def start_requests(self):
        yield scrapy.Request(url=self.start_url, callback=self.parse)

    def parse(self, response):
        print(response.url)
