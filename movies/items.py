# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from w3lib.html import remove_tags


class MoviesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class MovieItemLoader(ItemLoader):
    # 自定义itemloader,值取数组的第一个，修改item中的loader
    default_output_processor = TakeFirst()


def remove_fuhao(value):
        new_value = value.replace("\n", '').replace("\t", '').strip()
        return new_value


class MovieDetailItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    score = scrapy.Field(input_processor=MapCompose(remove_tags, remove_fuhao))
    actors = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_fuhao),
        output_processor=Join(' ')
    )
    dec = scrapy.Field()
    bofang_nums = scrapy.Field()
    movie_img_url = scrapy.Field()

    def get_insert_sql(self):
        # 执行具体的插入
        if 'actors' in self.keys():
            pass
        else:
            self['actors'] ='暂无'
        insert_sql = """
               insert into movie_detail(name,url,score,actors,decs,bofang_nums,movie_img_url) VALUES(%s,%s,%s,%s,%s,%s,%s) 
               """
        params = (self["name"], self["url"], self["score"], self["actors"],
                  self["dec"],self["bofang_nums"], self["movie_img_url"],
                  )
        return insert_sql, params
