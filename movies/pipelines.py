# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json

from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors

class MoviesPipeline(object):
    def process_item(self, item, spider):
        return item

class MysqlTwistedPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    # 导入setting中的配置（固定函数）
    @classmethod
    def from_settings(cls, setting):
        # 将dbtool传入
        dbparms = dict(
            host=setting["MYSQL_HOST"],
            db=setting["MYSQL_DBNAME"],
            user=setting["MYSQL_USER"],
            password=setting["MYSQL_PASSWORD"],
            charset="utf8",
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        # twisted异步容器，使用MySQldb模块连接
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)

        return cls(dbpool)

    def process_item(self, item, spider):
        # 使用Twisted将mysql插入变成异步执行
        query = self.dbpool.runInteraction(self.do_insert, item)
        # 处理异常
        query.addErrback(self.handle_error, item, spider)

    def handle_error(self, failure, item, spider):
        print(failure)
        # for k,v in item.items():
        #     print(k,v)
        print("出错了")

    def do_insert(self, cursor, item):
        # 执行具体的插入
        # inser_sql = """
        #        insert into articles(title,url,url_object_id,font_img_url,font_img_path,create_time,fa_num,sc_num,pinglun_num,tag,content)
        #        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        #        """
        # cursor.execute(inser_sql, (item["title"], item["url"], item["url_object_id"],
        #                            item["front_image_url"], item["front_image_path"], item["create_date"],
        #                            item["praise_nums"], item["fav_nums"], item["comment_nums"], item["tags"],
        #                            item["content"]))
        insert_sql, params = item.get_insert_sql()
        cursor.execute(insert_sql, params)

