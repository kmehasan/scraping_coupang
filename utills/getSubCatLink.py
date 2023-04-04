from bs4 import BeautifulSoup as bs
from lxml import etree
import sys
from utils import translate
links= []
def getProduct(soup):
    category = soup.select('.beauty')[0].select('.second-depth-list')#('//*[@class="beauty"]//*[@class="second-depth-list"]')
    for c in category:
        c_name = translate(c.find('a').text)
        for sub in c.select('.third-depth-list')[0].select('li'):
            sub_name = translate(sub.find('a').text)
            link = sub.find('a').get('href')
            links.append(f"{c_name},{sub_name},{link}")
            print(c_name,sub_name)
    with open('data/subCatLinks.csv', 'w', encoding='utf-8') as f:
        for link in links:
            f.write(link+"\n")
    
with open('data/category.html', 'r', encoding='utf-8') as f:

    contents = f.read()

    soup = bs(contents, 'lxml')
    getProduct(soup)