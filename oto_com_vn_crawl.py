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

cars = {}


for i in range(1, 2):

    html_text = requests.get('{}/p{}'.format(toyota_url, i)).text
    soup = bs(html_text, 'html.parser')
    box_list_car = soup.find('div', class_='box-list-car')
    item_cars = box_list_car.find_all('div', class_=re.compile(r'item-car'))

    href_ls = []

    for item in item_cars:
        href = item.find('a')['href']
        # print('{}{}'.format(base_url, href))
        href_ls.append('{}{}'.format(base_url, href))

for href in href_ls:
    html_text = requests.get(href).text
    soup = bs(html_text, 'html.parser')

    box_detail = soup.find('div', class_='box-detail-listing', id='box-detail')

    price = box_detail.find('input', id='price')['value']
    seats = box_detail.find('input', id='numberOfSeat')['value']
    # year = box_detail.find('input', id='year')['value']
    # typeOfCar = box_detail.find('input', id='classificationName')['value']

    group_title_detail = soup.find('div', class_='group-title-detail')
    name = group_title_detail.find('h1').string

    box_info_detail = soup.find('div', class_='box-info-detail')
    li = box_info_detail.find_all('li')
    print(len(li))











