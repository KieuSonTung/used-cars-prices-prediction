from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import re


class OtoCrawl:
    def __init__(self, base_url):
        self.base_url = base_url

    #  Input 1 page cua 1 hang xe
    def crawl_href(self, url):
        html_text = requests.get(url).text
        soup = bs(html_text, 'html.parser')
        box_list_car = soup.find('div', class_='box-list-car')
        item_cars = box_list_car.find_all('div', class_=re.compile(r'item-car'))

        href_ls = []

        for item in item_cars:
            href = item.find('a')['href']
            print('{}{}'.format(self.base_url, href))
            href_ls.append('{}{}'.format(self.base_url, href))

        return href_ls
