import requests
import urllib.request
from bs4 import BeautifulSoup

r = requests.get("https://companiesmarketcap.com/")

soup = BeautifulSoup(r.content, features="html.parser")


def save_image(url, ticker):
    response = requests.get(url)
    with open(f"/Users/matvejdoroshenko/rendering_bot/photos/second_screen/crypto_logos/{ticker}.png", "wb") as f:
        f.write(response.content)


cmkt = soup.find("body", "cmkt")
table_container_shadow = cmkt.find("div", "table-container shadow")
default_table = table_container_shadow.find("table", "default-table table marketcap-table dataTable")
tbody = default_table.find("tbody")
image_links = []
tickers = []
name_td = tbody.find_all("td", "name-td")
for el in name_td:
    logo_container = el.find("div", "logo-container")
    company_logo = logo_container.find("img", "company-logo")["src"]
    name_div = el.find("div", "name-div")
    a_tag = name_div.find("a")
    tickers.append(a_tag.find("div", "company-code").contents[1])
    image_links.append("https://companiesmarketcap.com/" + company_logo)

for x, y in zip(image_links, tickers):
    save_image(x, y)
