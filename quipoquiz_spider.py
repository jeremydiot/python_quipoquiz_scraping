import scrapy

class QuipoquizSpiderSpider(scrapy.Spider):
  name = 'quipoquiz_spider'
  allowed_domains = ['quipoquiz.com']
  start_urls = ['https://quipoquiz.com/fr/tous-les-quiz']

  custom_settings={
    "FEED_EXPORT_ENCODING": 'utf-8'
  }

  def parse(self, response):
    for item in response.css('.type_list_item'):
      quiz_link = item.css('a::attr(href)').get()
      image_link = item.css('img::attr(data-lazyload-src)').get()
      label = item.css('img::attr(alt)').get()
      quiz_full_link = "https://"+self.allowed_domains[0]+quiz_link
      
      yield scrapy.Request(quiz_full_link, callback=self.parse_quizId, cb_kwargs={
        'quiz_link':quiz_link,
        'image_link':image_link,
        'label':label.strip()
      })    

  def parse_quizId(self, response, quiz_link, image_link, label):
    
    quiz_id=response.css('meta[name=sednove_uid]::attr(content)').get()
    
    yield{
      'quiz_link':quiz_link,
      'image_link':image_link,
      'label':label,
      'quiz_id':quiz_id
    }