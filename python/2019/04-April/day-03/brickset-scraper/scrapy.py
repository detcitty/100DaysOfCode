import scrapy

class BrickSetSprider(scrapy.Spider):
        name = "brickset_spider"
        start_urls = ['http://brickset.com/sets/year-2016']
