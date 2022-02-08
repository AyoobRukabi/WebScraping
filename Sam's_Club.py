import requests
from bs4 import BeautifulSoup
import pandas as pd


baseurl = "https://www.samsclub.com"

headers = {
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/89.0.4389.128 Safari/537.36 '
}
products_links = []

for x in range(0, 1728, 48):
    r = requests.get(f'https://www.samsclub.com/s/health%20and%20beauty?offset={x}')

    soup = BeautifulSoup(r.content, 'lxml')
    products_list = soup.find_all('div', {"class": 'sc-pc-medium-desktop-card sc-plp-cards-card'})
    for link in products_list:
        links = link.find('a', href=True)
        products_links.append(baseurl + links['href'])


counter = 0
whiskylist = []
for link in products_links:
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    try:
        name = soup.find('h1').text.strip()
    except:
        name = 'no name'
    try:
        price = soup.find('span', class_="Price-group").text.strip().split()[2][:6]
    except:
        price = 'No Price'
    whisky = {
        'name': name,
        'price': price
         }
    whiskylist.append(whisky)
    counter += 1
    print(counter,': ', whisky['name'], ' | ', whisky['price'])
    df = pd.DataFrame(whiskylist)
    # print(df.head(len(whiskylist)))
    df.to_csv("health and beauty new.csv", sep=",", encoding='utf-8', index=False)

