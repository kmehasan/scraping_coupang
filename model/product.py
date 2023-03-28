import json
import utils
from googletrans import Translator
# pip3 install googletrans==3.1.0a0
class Product():
    translator = Translator()
    def __init__(self, name,nameKo, price_before_dc,price_after_dc, category,category2,brand,brandKo,thumbs,main_img,capacity,capacity2,desc,CoupangProductNumber,KeySpecifications,textBetween,link):
        self.name = name
        self.nameKo = nameKo
        self.price_after_dc = price_after_dc
        self.price_before_dc = price_before_dc
        self.category = category
        self.category2 = category2
        self.brand = brand
        self.brandKo = brandKo
        self.thumbs = thumbs
        self.main_img = main_img
        self.capacity = capacity
        self.capacity2 = capacity2
        self.desc = desc
        self.CoupangProductNumber = CoupangProductNumber
        self.KeySpecifications = KeySpecifications
        self.textBetween = textBetween
        self.link = link
        numbers = self.CoupangProductNumber.split(" - ")
        self.sku = "SKU_"+utils.base36encode(int(numbers[0])) + "_" + utils.base36encode(int(numbers[1]))
    def translate(self):
        self.name = self.translator.translate(self.name).text
        self.price_after_dc = self.translator.translate(self.price_after_dc).text
        self.price_before_dc = self.translator.translate(self.price_before_dc).text
        self.category = self.translator.translate(self.category).text
        self.category2 = self.translator.translate(self.category2).text
        self.brand = self.translator.translate(self.brand).text
        self.capacity = self.translator.translate(self.capacity).text
        self.capacity2 = self.translator.translate(self.capacity2).text
        self.desc = self.translator.translate(self.desc).text
        self.KeySpecifications = self.translator.translate(self.KeySpecifications).text
        self.textBetween = self.translator.translate(self.textBetween).text
        return self
        
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4,ensure_ascii=False)
