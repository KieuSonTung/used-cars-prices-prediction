from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import re

df = pd.DataFrame(columns=["name", "source_url", "origin", "km_driven",
                           "external_color", "seats", "engine_capacity",
                           "fuels", "transmission", "wheel_drive",
                           "price", "year"])

base_url = 'https://oto.com.vn'
toyota_url = 'https://oto.com.vn/mua-ban-xe-toyota'


for i in range(1, 102):

    html_text = requests.get('{}/p{}'.format(toyota_url, i)).text
    soup = bs(html_text, 'html.parser')
    box_list_car = soup.find('div', class_='box-list-car')
    item_cars = box_list_car.find_all('div', class_=re.compile(r'item-car'))

    href_ls = []

    for item in item_cars:
        href = item.find('a')['href']
        print('{}{}'.format(base_url, href))
        href_ls.append('{}{}'.format(base_url, href))



