import scrapy #imports scrapy package 

class EarSpider(scrapy.Spider):  #class inherits from scrapy, and inside scrapy inherits from Spider
    name = 'drugs' #name of spider
    start_urls = ['https://www.formularycomplete.com/report/public/THCCG-eBNF/83011'] #list urls to scrape

    def parse(self, response): #creating method parse self reference and response which contains the source code of the website to scrape
        
         for drugs in response.css('tr'):
                
                #retrieve data according to the aprropriate td html element 
                	yield {
                   'drugName' : drugs.css('td.drug-title::text').get(),
                   'status' : drugs.css('td.drug-status > span.badge.badge-custom::text').get().replace('\n    ','').replace('\n  ',''),
                   'presentation' : drugs.css('td.mf-title::text').get().replace('\n    ','').replace('\n  ',''),
                   'brandName' : drugs.css('td.prep-title > span.prep-space::text').get().relace('\n          ','').replace('\n        ','')
                   
                	   
                    }  

               
        
    		
               
    		

    		