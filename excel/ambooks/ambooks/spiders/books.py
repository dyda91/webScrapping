import scrapy


class BooksamazonSpider(scrapy.Spider):
    name = 'books'
    start_urls = ['https://www.amazon.com.br/gp/new-releases/books/ref=zg_bsnr_pg_2?ie=UTF8&pg={i}' for i in range(1,2)]

    def parse(self, response):
        for i in response.xpath('//div[@id="gridItemRoot"]'):
            title = i.xpath('.//div[@class="_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y"]//text()').get()
            price = i.css('.//span[@class="_cDEzb_p13n-sc-price_3mJ9Z"]//text()').get()
            image = i.xpath('.//div[@class="a-section a-spacing-mini _cDEzb_noop_3Xbw5"]//img/@src').get()
            link = i.xpath('.//a/@href').get()

            yield{
                'price': price,
                'title': title,
                'image': image,
                'link' : link
            }

        next_page = response.xpath('//a[contains(@title, "Próxima página")]/@href').get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)