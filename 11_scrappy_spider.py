import scrapy
class BasicSpider(scrapy.Spider):
   name = 'basic'
   allowed_domains = ['web']
   start_urls = ['https://sfbay.craigslist.org/search/sfc/apa']

   def parse(self, response):
       self.log("titles: {}".format(response.xpath('//span/text()').extract()))
       self.log("date: {}.".format(response.xpath('//*[@class="result-date"][1]/text()').extract()))
       self.log("urls: {}".format(response.xpath('//*[@class="result-title hdrlnk"][1]/@href').extract()))
       self.log("price: {}".format(response.xpath('//*[@class="result-price"][1]/text()').extract()))
       self.log("description is {}".format(response.xpath('//*[@class="result-hood"][1]/text()').extract()))
