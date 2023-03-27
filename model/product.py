class Product():
    def __init__(self, name,nameKo, price_before_dc,price_after_dc, category,category2,brand,brandKo,thumbs = [],main_img = [],capacity,capacity2,desc,CoupangProductNumber,KeySpecifications,textBetween):
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
