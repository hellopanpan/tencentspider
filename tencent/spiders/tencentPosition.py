# -*- coding: utf-8 -*-
import scrapy
from tencent.items import tencentItem

class TencentpositionSpider(scrapy.Spider):
    name = 'tencentPosition'
	url = "http://hr.tencent.com/position.php?start="
	offset = 0
    allowed_domains = ['tencent.com']
    start_urls = [url + str(offset)]

    def parse(self, response):
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']")
			#init the item modal
			item = tencentItem()
			item["name"] = each.xpath("./td[1]/a/text()").extract()[0]
			item["positionLink"] = each.xpath("./td[1]/a/@href").extract()[0]
			item["postionType"] = each.xpath("./td[2]/text()").extract().[0]
			item["peopleNum"] = each.xpath("./td[3]/text()").extract().[0]
			item["workLocation"] = each.xpath("./td[4]/text()").extract().[0]
			item["publishTime"] = each.xpath("./td[5]/text()").extract().[0]
