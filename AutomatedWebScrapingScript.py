import requests
from bs4 import BeautifulSoup

url = 'https://scrapingclub.com/exercise/list_basic/'
response = requests.get(url)
soup = BeautifulSoup(response.text,features= "html.parser")
items = soup.findAll('div',class_='col-lg-4 col-md-6 mb-4')
count =1
for i in items:
    itemName = soup.find('h4',class_='card-title').text.strip('\n')
    itemPrice = soup.find('h5').text
    count = count + 1

pages = soup.find('ul',class_='pagination')
urls=[]
links = soup.find_all('a',class_='page-link')
for link in links:
    pageNumb = int(link.text) if link.text.isdigit() else None
    if pageNumb != None:
        x = link.get('href')
        urls.append(x)
for i in urls:
    newURL = url + i
    response = requests.get(newURL)
    soup = BeautifulSoup(response.text, features="html.parser")
    items = soup.findAll('div', class_='col-lg-4 col-md-6 mb-4')
    count = 1
    for i in items:
        itemName = soup.find('h4', class_='card-title').text.strip('\n')
        itemPrice = soup.find('h5').text
        print(f"{count}, Price : {itemPrice}, Name :{itemName}")
        count = count + 1

