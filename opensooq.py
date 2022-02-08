import requests
from bs4 import BeautifulSoup
import pandas as pd

baseurl = "https://iq.opensooq.com"

headers = {
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/89.0.4389.128 Safari/537.36 '
}
products_links = []
products_id_list = []
whiskylist = []

for x in range(0, 1):
    r = requests.get(f'https://iq.opensooq.com/ar/%D8%B9%D9%82%D8%A7%D8%B1%D8%A7%D8%AA-%D9%84%D9%84%D8%A8%D9%8A%D8%B9/%D8%B4%D9%82%D9%82-%D9%84%D9%84%D8%A8%D9%8A%D8%B9?page={x}')
    soup = BeautifulSoup(r.content, 'html.parser')

    
    products_link = soup.find_all('div', {"class": 'rectLiDetails tableCell vMiddle p8'})
    for link in products_link:
        links = link.find('a', href=True)
        products_links.append(baseurl + links['href'])


# print(products_links)
# print(len(products_links))

counter = 0
whiskylist = []
for link in products_links:
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    
    try:
        name = soup.find('h1').text.strip()
    except:
        name = 'no name'

    info = soup.find('span', class_="blue").text.strip()
    print(info)
    description = soup.find('p', class_="firstPart breakWord").text
    print(description)

    whisky = {
        'name': name,
        'info': info,
        'description': description
         }
    whiskylist.append(whisky)
    counter += 1
    print(counter, ': ', whisky['name'], ' | ', whisky['info'], ' | ', whisky['description'])
df = pd.DataFrame(whiskylist)
print(df)
df.to_csv("opensooq6.csv", sep=",", encoding="utf-8-sig", index=False)


