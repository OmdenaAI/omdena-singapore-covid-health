import scrapy
from ..items import CnascraperItem

items = CnascraperItem()

class CNASpider(scrapy.Spider):
    name = "cna_spider"

    def start_requests(self):
        for i in range(51):
            yield scrapy.Request(
                url = f"https://www.channelnewsasia.com/archives/8396078/news?pageNum={i}&channelId=7469254",
                callback = self.parse)

    def parse(self, response):
        titles_link = response.xpath('//h3[@class="teaser__heading"]/a/@href')
        titles_link_ext = titles_link.extract()

        for url in titles_link_ext:
            yield response.follow(url = url, callback = self.parse_article)

    def parse_article(self, response):
        title = response.xpath('//h1[@class="article__title"]/text()').extract_first()

        if any(kw in title for kw in ["Mental", "mental",
                                      "Depression", "depression", "Anxiety",
                                      "anxiety", "Lonely", "lonely", "Suicide", "suicide"]):

            texts = response.xpath('//div[@class="c-rte--article"]//p/text()').extract()
            full_text = " ".join(texts)
            author = response.xpath('//div[@class="article__author-details"]/a/text()')[1].extract().strip()
            date = response.xpath('//time[@class="article__details-item"]/text()').extract_first()

            items['title'] = title
            items['author'] = author
            items['text'] = full_text
            items['date'] = date
            items['url'] = response

            yield items
