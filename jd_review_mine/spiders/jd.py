# -*- coding: utf-8 -*-
import scrapy
import logging
import datetime
import random, time, requests, json
from scrapy.selector import Selector
from jd_review_mine.items import JdReviewMineItem

class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']

    def __init__(self, keyword, sku=None, *args, **kwargs):
        """jd搜索页面后一半是动态加载，需要访问php接口"""
        super(JdSpider, self).__init__(*args, **kwargs)
        self.start_url_1 = 'https://search.jd.com/Search?keyword={}'.format(keyword)
        self.start_url_2 = 'https://search.jd.com/s_new.php?keyword={}'.format(keyword)
        self.comment_url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId={}&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&rid=0&fold=1'

    def start_requests(self):
        """第一层，搜索商品链接得到的第一页数据"""
        yield scrapy.Request(url=self.start_url_1, callback=self.parse)
        yield scrapy.Request(url=self.start_url_2, callback=self.parse, meta={'reference':self.start_url_1})

    def parse(self, response):
        """解析商品：唯一sku标识， 价格price, 标题title"""
        goods_list = response.xpath('//*[@id="J_goodsList"]/ul/li')
        for good in goods_list:
            sku = good.xpath('@data-sku').get()
            price = good.xpath('div/div[3]/strong/i/text()').get()
            title = good.xpath('div/div[4]/a/em/text()').get()
            if len(title)<10:
                title = good.xpath('div/div[4]/a/em/text()').getall()[1]
            params = {
                'sku': sku,
                'price': price,
                'title': title,
                'page': 0
            }
            first_comment_url = self.comment_url.format(sku,0)
            yield scrapy.Request(url=first_comment_url, callback=self.comment_parse,meta=params)

    def comment_parse(self,response):
        item = JdReviewMineItem()
        comment_json = json.loads(response.text[20:-2])
        comments = comment_json['comments']
        params = response.meta
        item['sku'] = params['sku']
        item['price'] = params['price']
        item['title'] = params['title']
        for comment in comments:
            item['id'] = comment['id']
            item['content'] = comment['content']
            item['score'] = comment['score']
            item['plus'] = comment['plusAvailable']
            item['nickname'] = comment['nickname']
            item['creationTime'] = comment['creationTime']
            yield item
        max_page = comment_json['maxPage']
        if params['page']<max_page:
            params['page'] +=1
            next_comment_url = self.comment_url.format(params['sku'], params['page'])
            yield scrapy.Request(url=next_comment_url, callback=self.comment_parse,meta=params)
        else:
            print('sku：{} finished'.format(params['sku']))











