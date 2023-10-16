import requests
from bs4 import BeautifulSoup

url = 'https://www.lamoda.ru/catalogsearch/result/?q=nike%20jordan&submit=y&gender_section=women'
r = requests.get(url)
text = r.text
print(text)

soup = BeautifulSoup(r.text, "html.parser")

products = soup.find_all("div", class_="x-product-card-description__product-name")
for product in products:
    print(product.text)
