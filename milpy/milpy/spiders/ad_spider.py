import scrapy
from ..items import MilpyItem
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager    # pip install webdriver-manager
# from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
import time


class AdSpider(scrapy.Spider):
    name = 'ads'
    start_urls = [
        'https://www.milanuncios.com/coches-de-segunda-mano/pagina=1'
    ]
    download_delay = 1.0

    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        # self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.total_pages = 350
        self.current_page = 1
        self.links = []
        self.base_url = 'https://www.milanuncios.com/coches-de-segunda-mano/pagina='
        self.count_link = 0

    def parse(self, response):

        self.driver.get(response.url)

        # Scroll to page bottom to load whole page
        SCROLL_PAUSE_TIME = 0.4
        scroll = 400
        for i in range(1, 15):
            # scroll down
            scroll = scroll + 1100
            self.driver.execute_script("window.scrollTo(0, " + str(scroll) + ");")
            # wait to load page
            time.sleep(SCROLL_PAUSE_TIME)
            # repeat until page bottom

        # Collect all product links
        # Parse links to collect product info
        for ad_link in self.driver.find_elements(By.CSS_SELECTOR, "h2.ma-AdCard-title-text > a"):
            self.links.append(ad_link.get_attribute("href"))
        self.links = list(set(self.links))

        if self.current_page == self.total_pages:
            for link in self.links:
                self.count_link += 1
                yield response.follow(link, callback=self.parse_ad)
        else:
            self.current_page += 1
            next_page = self.base_url + str(self.current_page)
            # self.restore_driver(next_page)
            yield response.follow(next_page, callback=self.parse)



    def parse_ad(self, response):

        items = MilpyItem()

        # price tag is dinamically loaded (requires javascript) with bot protection
        # use selenium to retrieve price tag
        self.driver.get(response.url)
        soup = bs(self.driver.page_source, "lxml")
        price = soup.find("span",
                          class_="ma-AdPrice-value ma-AdPrice-value--default ma-AdPrice-value--heading--l").text.replace(
            '\xa0€', '').replace('.', '')

        # retrive remaining tags from scrapy response
        title = response.css('h1.ma-AdDetail-title.ma-AdDetail-title-size-heading-m::text').get()
        ref_num = response.css('span.ma-AdDetail-metadata-reference::text').get().replace('Ref: ', '')
        location = response.css('address.ma-AdDetail-metadata-location.ma-AdDetail-metadataTag::text').get().replace(
            ' (', '').replace(')', '')
        info = response.css('span.ma-AdTag-label::text').getall()
        if info[0] == 'Profesional':
            seller = info[0]
            color = info[1]
            door_num = info[2].replace(' puertas', '')
            year = info[-1].replace('año ', '')
            if "Etiqueta" in info[3]:
                fuel_type = info[4]
                hp = info[5].replace('cv', '')
                mileage = info[6].replace('km', '').replace('.', '')
                transmission = info[7]
            else:
                fuel_type = info[3]
                hp = info[4].replace('cv', '')
                mileage = info[5].replace('km', '').replace('.', '')
                transmission = info[6]
        else:
            seller = 'Particular'
            color = info[0]
            door_num = info[1].replace(' puertas', '')
            year = info[-1].replace('año ', '')
            if "Etiqueta" in info[2]:
                fuel_type = info[3]
                hp = info[4].replace('cv', '')
                mileage = info[5].replace('km', '').replace('.', '')
                transmission = info[6]
            else:
                fuel_type = info[2]
                hp = info[3].replace('cv', '')
                mileage = info[4].replace('km', '').replace('.', '')
                transmission = info[5]

        items['title'] = title
        items['price'] = price
        items['ref_num'] = ref_num
        items['location'] = location
        items['seller'] = seller
        items['color'] = color
        items['door_num'] = door_num
        items['fuel_type'] = fuel_type
        items['hp'] = hp
        items['mileage'] = mileage
        items['transmission'] = transmission
        items['year'] = year

        yield items
