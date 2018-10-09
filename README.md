# scrapy_movie
scrapy爬取腾讯所有热播电影相关信息

主要小问题：
    1.数据库的字段命名如果和保留字有冲突，记得给字段加单引号，具体字段可参考博客https://www.cnblogs.com/henuyuxiang/p/6811693.html；
    2.该爬取实例化item用的loader_item，有的电影主演为空（如动漫熊出没等），则item实例化后无主演（actors）这个键，因此需要判断是否有该键并做相应处理；
   
总的来说，是很简单的一个例子，代码量小，只需注意细节即可。
