from model.product import Product
import utills.utils as utils
import json

with open('data/productDetailsEdit.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    products = []
    skus = []
    for i in data:
        product = Product(i['name'], i['nameKo'], i['price_after_dc'], i['price_before_dc'], i['category'], i['category2'], i['brand'], i['brandKo'], i['thumbs'], i['main_img'], i['capacity'], i['capacity2'], i['desc'], i['CoupangProductNumber'], i['KeySpecifications'], i['textBetween'], i['link'])
        main_images = i['main_img']
        thumbs = i['thumbs']
        if i['sku'] in skus:
            print("Duplicate sku")
            continue
        with open('data/images.json', 'a+', encoding='utf-8') as f:
            n = 1
            new_main_images = []
            for img in main_images:
                img_name = i['sku']+"_"+str(n)
                new_main_images.append(img_name)
                f.write(img_name)
                f.write(':')
                f.write(img)
                f.write('\n')
                n += 1
            product.main_img = new_main_images

            new_thumbs = []
            for img in thumbs:
                img_name = i['sku']+"_"+str(n)
                new_thumbs.append(img_name)
                f.write(img_name)
                f.write(':')
                f.write(img)
                f.write('\n')
                n += 1
            product.thumbs = new_thumbs
        products.append(product.toJSON())
    with open('data/products.json', 'w', encoding='utf-8') as f:
        f.write('[\n')
        for i in products:
            f.write(i)
            f.write(',\n')
        f.write(']')

            