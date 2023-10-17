Kareva Alena: 20%
Makeeva Angelina 10%

import requests
from bs4 import BeautifulSoup

url = 'https://www.lamoda.ru/catalogsearch/result/?q=nike%20jordan&submit=y&gender_section=women'
r = requests.get(url)
text = r.text

with open("end.txt", "w", encoding="utf-8") as file:
    file.write(text)
    file.write("\n")  

soup = BeautifulSoup(r.text, "html.parser")

products = soup.find_all("div", class_="x-product-card-description__product-name")
with open("end.txt", "a", encoding="utf-8") as file:
    for product in products:
        file.write(product.text)
        file.write("\n")

brands = soup.find_all("div", class_="x-product-card-description__brand-name")
with open("end.txt", "a", encoding="utf-8") as file:
    for brand in brands:
        file.write(brand.text)
        file.write("\n")

prices = soup.find_all("div", class_="x-product-card-description__microdata-wrap")
with open("end.txt", "a", encoding="utf-8") as file:
    for price in prices:
        file.write(price.text)
        file.write("\n")

