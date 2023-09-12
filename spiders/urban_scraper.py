import scrapy
from urban.items import WordItem

class UrbanScraperSpider(scrapy.Spider):
    name = "urban_scraper"
    allowed_domains = ["www.urbandictionary.com"]
    start_urls = ["https://www.urbandictionary.com/"]

    def parse(self, response):
        words = response.css("div.definition")
        for word in words:
            title = word.css("a.word::text").get()
            definition = word.css("div.meaning *::text").getall()
            definition = " ".join(definition)
            item = WordItem()
            item["word"] = title 
            item["definition"] = definition
            yield item

        next = response.css("a[rel='next']").attrib["href"]
        yield response.follow(next, self.parse)
