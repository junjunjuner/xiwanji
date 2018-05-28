# -*- coding: utf-8 -*-

# Scrapy settings for xiwanji project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'xiwanji'

SPIDER_MODULES = ['xiwanji.spiders']
NEWSPIDER_MODULE = 'xiwanji.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
jd_user_agent=[
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32
RETRY_ENABLED=True
RETRY_TIMES=5                #重试次数
# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY =2                 #下载延迟
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16                #并发数

# Disable cookies (enabled by default)
COOKIES_ENABLED = False                    #关闭cookies

DOWNLOADER_MIDDLEWARES = {
#    'gome.middlewares.MyCustomDownloaderMiddleware': 543,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'xiwanji.middlewares.JdUseragentMiddleware': 400,
    # 'jdjinshuiji.middlewares.Exceptions': 300
}

ITEM_PIPELINES = {
    'xiwanji.pipelines.MongoPipeline': 300,
    'xiwanji.pipelines.CSVPipeline': 200

}

#水槽式洗碗机
FIELDS_TO_EXPORT = [
    'p_Name',               #商品名称
    'shop_name',            #店铺名称
    'ProductID',            #商品ID
    'price',                #原价
    'PreferentialPrice',    #折扣价
    'CommentCount',         #评论总数
    'GoodRateShow',         #好评率
    'GoodCount',            #好评
    'GeneralCount',         #中评
    'PoorCount',            #差评
    'keyword',              #评论关键字
    'type',                 #商品详情
    'brand',                #品牌
    'X_name',               #型号
    'open_method',          #开合方式
    'laundry',              # 洗涤方式
    'capacity',             # 餐具容量
    'control',              #控制方式
    'dry_method',           #干燥方式
    'disinfection',         #消毒方式
    'consump',              #耗水量
    'color',                #颜色
    'product_url',          #商品链接
    'source',               #来源
    'ProgramStarttime'      #爬取时间
]

# AUTOTHROTTLE_ENABLED = True                    #开启自动限速算法
# The initial download delay
AUTOTHROTTLE_START_DELAY = 3
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60

# AUTOTHROTTLE_DEBUG = True                   #可看到是如何进行自动限速的

MONGO_HOST = "172.28.171.13"  # 主机IP
MONGO_PORT = 27017  # 端口号

# #水槽式洗碗机数据库
# MONGO_DB = "ShuiCaoXWJ"  # 库名
# MONGO_COLL = "shuicao_jd"  # 文档(相当于关系型数据库的表名)

#台式洗碗机数据库
MONGO_DB = "TaiShiXWJ"  # 库名
MONGO_COLL = "taishi_jd"  # 文档(相当于关系型数据库的表名)

# LOG_FILE='jd踢脚线_log_%s.txt' % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# LOG_FILE='jdjsq_log_%s.txt'% (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
RANDOMIZE_DOWNLOAD_DELAY=True
