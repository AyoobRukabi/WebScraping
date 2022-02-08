import requests
from bs4 import BeautifulSoup
import pandas as pd

baseurl = "https://orisdi.com/"

headers = {
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/89.0.4389.128 Safari/537.36 '
}
products_links = []
products_id_list = []
whiskylist = []

# for x in range(0, 35):
r = requests.get('https://orisdi.com/collections/electronics')
soup = BeautifulSoup(r.content, 'html.parser')

products_list = soup.find_all('div', {'id': 'product-loop'})
products_price = soup.find('span', class_="money conversion-bear-money").text
products_title = soup.find_all('p')
price = soup.find('p', id_="product-price")

products_link = soup.find_all('div', {"class": 'prod-image'})
for link in products_link:
    links = link.find('a', href=True)
    products_links.append(baseurl + links['href'])

#########################
print(products_links)
counter = 0
whiskylist = []
for link in products_links:
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    name = soup.find('h1').text
    # print(name)
    try:
        name = soup.find('h1').text
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
    df.to_csv("Orisdi1.csv", sep=",", encoding='utf-8', index=False)







# print(products_list)
# # print("==============================================================")
# # print(products_price)
# # print("==============================================================")
# # print(products_title)
# # print(price)
# print(products_link)
# print(products_links)


    #     # product_price = soup.find_all('p', class_='product-card__price') # test
    #     print(products_price)
    #     for price in products_price:
    #         products_id_list.append(price.get('title'))
    #
    #     whisky = {
    #             'prod-price': prod_price,
    #             'title': title
    #                 # 'price': price,
    #                 # 'paragraph': paragraph
    #             }
    #     whiskylist.append(whisky)
    #     count += 1
    #     print(count, ': ', whisky['title'])
    # df = pd.DataFrame(whiskylist)
    # # print(df.head(len(whiskylist)))
    # df.to_csv("health and beauty22.csv", sep=",", encoding='utf-8', index=False)
    #
