# -*- coding: utf-8 -*-
import scrapy
from ..items import QuotesItem

class QuotesCrawlSpider(scrapy.Spider):
    name = 'quotes_crawl'
    allowed_domains = ['toscrape.com/']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        items = QuotesItem()

        all_div_quotes = response.css('div.quote')

        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag
        
            yield items
        
        next_page = response.css('li.next a::attr(href)').get()

        if next_page:
            next_page = 'http://quotes.toscrape.com' + next_page            
            yield scrapy.Request(next_page, callback=self.parse,dont_filter=True)