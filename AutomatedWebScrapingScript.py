import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl.workbook import Workbook


data= []
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
# Go thru all page itself and extract data.
for link in links:
    pageNumb = int(link.text) if link.text.isdigit() else None
    if pageNumb != None:
        x = link.get('href')
        urls.append(x)
# Scaping all data from file
for i in urls:
    newURL = url + i
    response = requests.get(newURL)
    soup = BeautifulSoup(response.text, features="html.parser")
    items = soup.findAll('div', class_='col-lg-4 col-md-6 mb-4')
    count = 1
    for i in items:
        item={}
        item['itemName'] = soup.find('h4', class_='card-title').text.strip('\n')
        item['itemPrice'] = soup.find('h5').text
        print(f"{count}, Price : {itemPrice}, Name :{itemName}")
        data.append(item)
        count = count + 1
# export data into excel file
def export(data):
    df = pd.DataFrame(data)
    df.to_excel("scraped_data_file.xlsx")


export(data)