from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from oto_comvn_class import OtoCrawl
import re

df = pd.DataFrame(columns=["name", "source_url", "origin", "km_driven",
                           "external_color", "seats", "engine_capacity",
                           "fuels", "transmission", "wheel_drive",
                           "price", "year"])

base_url = 'https://oto.com.vn'
toyota_url = 'https://oto.com.vn/mua-ban-xe-toyota'

href_df = pd.read_csv('oto_comvn_href.csv')

for href in href_df['href']:
    html_text = requests.get(href)
    # soup = bs(html_text, 'html.parser')
    content = html_text.content
    soup = bs(content.decode('utf-8', 'ignore'), 'html.parser')

    box_detail = soup.find('div', class_='box-detail-listing', id='box-detail')

    price = box_detail.find('input', id='price')['value']
    seats = box_detail.find('input', id='numberOfSeat')['value']
    year = box_detail.find('input', id='year')['value']
    typeOfCar = box_detail.find('input', id='classificationName')['value']

    group_title_detail = soup.find('div', class_='group-title-detail')
    name = group_title_detail.find('h1').string

    box_info_detail = soup.find('div', class_='box-info-detail')
    li = box_info_detail.find_all('li')
    for l in li:
        txt = l.get_text()













