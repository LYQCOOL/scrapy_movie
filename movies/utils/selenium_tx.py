# _*_ encoding:utf-8 _*_
__author__ = 'LYQ'
__date__ = '2018/10/9 10:08'
from selenium import webdriver
browser=webdriver.Chrome()
from scrapy.selector import Selector
browser.get('https://film.qq.com/film_all_list/allfilm.html?type=movie')
selector=Selector(text=browser.page_source)
page_movies=selector.css('li.list_item')[1:]
# print(page_movies.extract())
images=page_movies.css('img::attr(src)').extract()
titles=page_movies.css('a::attr(title)').extract()
urls=page_movies.css('a::attr(href)').extract()
decs=page_movies.css('div.figure_desc::text').extract()
print(images,titles,urls,decs)
