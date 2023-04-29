from model.product import Product
import json
import db
mydb = db.MyDB()
def getImages(product):
    images = ''
    imgs = mydb.getUrlList(product.thumbs)
    if len(imgs) == 0:
        return ""
    for i in imgs:
        if 'product_images' not in i[0]:
            continue
        images += f'{i[0]}, '
    return images[:-1]
    # for i in product.thumbs:
    #     # images += f'https://www.celmadekorea.com/wp-content/uploads/product_images/images/{i}, '
    #     url = mydb.getUrl(i)
    #     if(url == ""):
    #         continue
    #     images += f'{url}, '
    # return images[:-1]

def getDescription(product):
    desc = ""
    imgs = mydb.getUrlList(product.main_img)
    for i in imgs:
        if 'product_images' not in i[0]:
            continue
        desc += f'<img src="{i[0]}" width="100%" />'
    return  desc
    # for i in product.main_img:
    #     # desc += f'<img src="https://www.celmadekorea.com/wp-content/uploads/product_images/main/{i}" alt="{i}" width="100%" />'
    #     url = mydb.getUrl(i)
    #     if(url == ""):
    #         continue
    #     desc += f'<img src="{url}" width="100%" />'
    # return desc
def getPrice(price):
    if(price == 'No discount'):
        return 0
    return price.replace(",","").replace("KRW ","").replace(" ","").replace("won","")
def getHeading():
    return '''Brand,Copang_number,Type,SKU,Name,Published,Is featured?,Visibility in catalog,Short description,Description,Tax status,In stock?,Backorders allowed?,Sold individually?,Allow customer reviews?,Sale price,Regular price,Categories,Images,Position,Attribute 1 name,Attribute 1 value(s),Attribute 1 visible,Attribute 1 global,Attribute 2 name,Attribute 2 value(s),Attribute 2 visible,Attribute 2 global'''
def getProdutRowString(product):    
    return f'{product.brand.title()},{product.CoupangProductNumber},"simple","{product.sku}","{product.name}","-1","0","visible","{product.desc}","{getDescription(product)}","taxable",1,0,0,1,"{getPrice(product.price_after_dc)}","{getPrice(product.price_before_dc)}","{product.category2.replace("Coupang Home > ","")}","{getImages(product)}",0,"KeySpecifications","{product.KeySpecifications}",1,0,"Capacity","{product.capacity2}",1,0'

with open('data/products_modified.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    unique_data = []
    count = 1
    for i in data:
        if i not in unique_data:
            unique_data.append(i)
    data = unique_data
    data_len = len(data)
    for chunk in range(0,len(data),1000):
        products = []
        output = getHeading()
        for i in data[chunk:chunk+1000]:
            print(count,'/',data_len, ' ', count/data_len*100, '%')
            count += 1
            product = Product(i['name'], i['nameKo'], i['price_after_dc'], i['price_before_dc'], i['category'], i['category2'], i['brand'], i['brandKo'], i['thumbs'], i['main_img'], i['capacity'], i['capacity2'], i['desc'], i['CoupangProductNumber'], i['KeySpecifications'], i['textBetween'], i['link'])
            output += '\n'+getProdutRowString(product)
        with open(f'data/products_modified_final_edit_{chunk}_{chunk+1000}.csv', 'w', encoding='utf-8') as f:
            f.write(output)

mydb.close()
