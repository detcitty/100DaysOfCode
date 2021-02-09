import scrapy

class WestVirigina(scrapy.Spider):
    name = "westvirginia_spider"
    start_urls = ["https://ohflac.wvdhhr.org/Apps/Lookup/FacilitySearch"]
