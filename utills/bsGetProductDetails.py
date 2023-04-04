from bs4 import BeautifulSoup as bs
from lxml import etree

def getProduct(soup):
    dom = etree.HTML(str(soup))
    name = dom.xpath("//*[@class='prod-buy-header__title']")[0].text
    nameKo = name
    price_after_dc = dom.xpath("//*[@class='total-price']")[0].text
    thumbs = [img for img in dom.xpath("//*[@class='prod-image__items']//img/@data-src")]
    mainImages = [img for img in dom.xpath("//*[@class='subType-IMAGE']//img/@data-src")]
    # category2 = dom.xpath("//*[@id='breadcrumb']")[0].text.replace("\n"," ")
    category2 = soup.find('ul', {'id' :'breadcrumb'}).text
    print(category2)
    category = ""#category2.split(">")[2].strip()
    brand = dom.xpath("//*[@class='prod-brand-name']")[0].text
    brandKo = brand

    capacity = dom.xpath("//*[@class='prod-option__selected-container']")[0].text.replace("\n"," ")
    capacity2 = dom.xpath('//*[@id="itemBrief"]/div/table/tbody/tr[1]/td[1]/font/font')[0].text.replace("\n"," ")
    descAll = dom.xpath("//*[@class='prod-description-attribute']//li")
    desc = "\n".join([li.text for li in descAll[1:-1]])
    CoupangProductNumber = descAll[-1].text.split(":")[1].strip()
    KeySpecifications = dom.xpath('//*[@id="itemBrief"]/div/table/tbody/tr[1]/td[2]/font/font')[0].text.replace("\n"," ")
    textBetween = ""
    
    try:
      price_before_dc = dom.xpath("//*[@class='origin-price']")[0].text
    except:
      price_before_dc = "No discount"
    
    print(f"name: {name} nameKo: {nameKo} price_after_dc: {price_after_dc} price_before_dc: {price_before_dc} category: {category} category2: {category2} brand: {brand} brandKo: {brandKo} thumbs: {thumbs} mainImages: {mainImages} capacity: {capacity} capacity2: {capacity2} desc: {desc} CoupangProductNumber: {CoupangProductNumber} KeySpecifications: {KeySpecifications} textBetween: {textBetween}")

with open('test.html', 'r', encoding='utf-8') as f:

    contents = f.read()

    soup = bs(contents, 'lxml')
    getProduct(soup)