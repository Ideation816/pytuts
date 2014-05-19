from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

class MySpider(BaseSpider):
    name = "cl"
    allowed_domains = ["craigslist.org"]
    start_urls = ["http://washingtondc.craigslist.org/mld/sof/"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select("//p")
        for titles in titles:
            title = titles.select("a/text()").extract()
            link = titles.select("a/@href").extract()
            print title, link