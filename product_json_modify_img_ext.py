from model.product import Product
import json
from glob import glob
all_images = glob('C:/Users/KME-Hasan/Downloads/compressed_main/*')
all_images.extend(glob('C:/Users/KME-Hasan/Downloads/compressed/*'))
all_images = [i.split('\\')[-1] for i in all_images]
extensions = [".webp",".jpg"]

with open('data/products.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    products = []
    for i in data:
        product = Product(i['name'], i['nameKo'], i['price_after_dc'], i['price_before_dc'], i['category'], i['category2'], i['brand'], i['brandKo'], i['thumbs'], i['main_img'], i['capacity'], i['capacity2'], i['desc'], i['CoupangProductNumber'], i['KeySpecifications'], i['textBetween'], i['link'])
        main_images = i['main_img']
        thumbs = i['thumbs']
        new_main_images = []
        for img in main_images:
            for ext in extensions:
                if img+ext in all_images:
                    new_main_images.append(img+ext)
                    break
        product.main_img = new_main_images
        new_thumbs = []
        for img in thumbs:
            for ext in extensions:
                if img+ext in all_images:
                    new_thumbs.append(img+ext)
                    break
        product.thumbs = new_thumbs
        products.append(product.toJSON())
    with open('data/products_modified.json', 'w', encoding='utf-8') as f:
        f.write('[\n')
        for i in products:
            f.write(i)
            f.write(',\n')
        f.write(']')