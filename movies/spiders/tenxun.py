# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from items import MovieDetailItem, MovieItemLoader


class TenxunSpider(scrapy.Spider):
    name = 'tenxun'
    allowed_domains = ['v.qq.com']
    start_urls = ['https://v.qq.com/x/list/movie']

    def parse(self, response):
        list_items = response.css('li.list_item')
        for list_item in list_items:
            item_loader = MovieItemLoader(item=MovieDetailItem(), selector=list_item)
            item_loader.add_css('name', '.figure_title a::attr(title)')
            item_loader.add_css('url', '.figure_title a::attr(href)')
            item_loader.add_css('score', '.figure_score')
            item_loader.add_css('actors', '.figure_desc a::text')
            item_loader.add_css('dec', '.figure_info::text')
            item_loader.add_css('bofang_nums', '.figure_count span::text')
            item_loader.add_css('movie_img_url', 'img::attr("r-lazyload")')
            print(item_loader.load_item())
            yield item_loader.load_item()
        next_url = response.css(".page_next::attr(href)").extract_first()
        if next_url:
            yield Request(self.start_urls[0] + next_url, callback=self.parse)
