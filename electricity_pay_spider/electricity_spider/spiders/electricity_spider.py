import scrapy
import helper.IterHelper


class ElectricitySpider(scrapy.Spider):
    name = "electricity"

    def fetch_option(self, param):
        levels = ['programId', 'txtyq', 'txtld']

    def update_data(self, response):
        __EVENTTARGET = response.xpath('//input[@name="__EVENTTARGET"]/@value').extract_first()
        __EVENTARGUMENT = response.xpath('//input[@name="__EVENTARGUMENT"]/@value').extract_first()
        __LASTFOCUS = response.xpath('//input[@name="__LASTFOCUS"]/@value').extract_first()
        __VIEWSTATE = response.xpath('//input[@name="__VIEWSTATE"]/@value').extract_first()
        __EVENTVALIDATION = response.xpath('//input[@name="__EVENTVALIDATION"]/@value').extract_first()
        self.data['__EVENTTARGET'] = __EVENTTARGET
        self.data['__EVENTARGUMENT'] = __EVENTARGUMENT
        self.data['__LASTFOCUS'] = __LASTFOCUS
        self.data['__VIEWSTATE'] = __VIEWSTATE
        self.data['__EVENTVALIDATION'] = __EVENTVALIDATION

    def start_requests(self):
        self.url = "http://202.114.18.218/main.aspx"
        self.data = {}
        yield scrapy.Request(self.url, callback=self.choose_area)


    def choose_area(self, response):
        options = []
        for option in response.xpath('//select[@id="programId"]/option'):
            option_val = option.xpath('./@value').extract_first()
            if "-1" not in option_val:
                options.append(option_val)
        print("Area Options: " + ",".join(options))

        self.update_data(response)
        self.data['__EVENTTARGET'] = 'programId'
        for option in options:
            self.data['programId'] = option
            req = scrapy.FormRequest(self.url, formdata=self.data, callback=self.choose_building)
            req.meta['area'] = option
            yield req
        # self.data['programId'] = '东区'
        # yield scrapy.FormRequest(self.url, formdata=self.data, callback=self.choose_building)

    def choose_building(self, response):
        options = []
        for option in response.xpath('//select[@id="txtyq"]/option'):
            optionVal = option.xpath('./@value').extract_first()
            if not "-1" in optionVal:
                options.append(optionVal)
        print("Building Options of " +  str(response.meta['area']) + ": " + ",".join(options))

        self.update_data(response)
        self.data['__EVENTTARGET'] = 'txtyq'
        # self.data['txtyq'] = '南二舍'
        # yield scrapy.FormRequest(self.url, formdata=self.data, callback=self.choose_room)
        for option in options:
            self.data['txtyq'] = option
            req = scrapy.FormRequest(self.url, formdata=self.data, callback=self.choose_room)
            req.meta['area'] = response.meta['area']
            req.meta['building'] = option
            yield req

    def choose_room(self, response):
        options = []
        for option in response.xpath('//select[@id="txtld"]/option'):
            optionVal = option.xpath('./@value').extract_first()
            if not "-1" in optionVal:
                options.append(optionVal)
        print("Room Options of " + response.meta['area'] + "_" + response.meta['building'] + ": " + ",".join(options))

        self.update_data(response)
        self.data['__EVENTTARGET'] = ''
        self.data['txtld'] = '4层'
        self.data['Txtroom'] = '401'
        self.data['ImageButton1.x'] = '15'
        self.data['ImageButton1.y'] = '15'
        yield scrapy.FormRequest(self.url, formdata=self.data, callback=self.fetch_result)

    def fetch_result(self, response):
        result = {}
        for option in response.xpath('//table[@id="GridView2"]/tr[td]'):
            time = option.xpath('./td[2]/text()').re(r'20([0-9-]*) .*')[0]
            data = option.xpath('./td[1]/text()').extract_first()
            print(time + ": " + data)
