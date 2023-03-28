from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from model.product import Product

options = webdriver.ChromeOptions()
# user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'
# options.add_argument('user-agent={0}'.format(user_agent))
# options.add_argument("--headless")
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
options.add_argument('user-agent={0}'.format(user_agent))
def getProductDetails():
    name = driver.find_element(By.XPATH,"//*[@class='prod-buy-header__title']").get_attribute("innerText")
    nameKo = driver.find_element(By.XPATH,"//*[@class='prod-share__twitter']").get_attribute("data-title")
    price_after_dc = driver.find_element(By.XPATH,"//*[@class='total-price']").get_attribute("innerText")
    thumbs = [img.get_attribute('src') for img in driver.find_elements(By.XPATH,"//*[@class='prod-image__items']//img")]
    mainImages = [img.get_attribute('src') for img in driver.find_elements(By.XPATH,"//*[@class='subType-IMAGE']//img")]
    category2 = driver.find_element(By.XPATH,"//*[@id='breadcrumb']").get_attribute("innerText").replace("\n"," ")
    category = category2.split(">")[2].strip()
    brand = driver.find_element(By.XPATH,"//*[@class='prod-brand-name']").get_attribute("innerText")
    brandKo = driver.find_element(By.XPATH,"//*[@class='prod-brand-name']").get_attribute("data-brand-name")

    capacity = driver.find_element(By.XPATH,"//*[@class='prod-option__selected-container']").get_attribute("innerText").replace("\n"," ")
    capacity2 = driver.find_element(By.XPATH,'//*[@id="itemBrief"]/div/table/tbody/tr[1]/td[1]').get_attribute("innerText").replace("\n"," ")
    descAll = driver.find_elements(By.XPATH,"//*[@class='prod-description-attribute']//li")
    desc = "\n".join([li.get_attribute("innerText") for li in descAll[1:-1]])
    CoupangProductNumber = descAll[-1].get_attribute("innerText").split(":")[1].strip()
    KeySpecifications = driver.find_element(By.XPATH,'//*[@id="itemBrief"]/div/table/tbody/tr[1]/td[2]').get_attribute("innerText").replace("\n"," ")
    textBetween = ""
    
    try:
      price_before_dc = driver.find_element(By.XPATH,"//*[@class='origin-price']").get_attribute("innerText")
    except:
      price_before_dc = "No discount"
    product = Product(name,nameKo,price_before_dc,price_after_dc,category,category2,brand,brandKo,thumbs,mainImages,capacity,capacity2,desc,CoupangProductNumber,KeySpecifications,textBetween,l)
    product = product.translate()
    print()
    print(name,nameKo,price_after_dc,price_before_dc)
    print()
    return product


with open("data/links.txt","r") as f:
    links = f.readlines()
    for l in links:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),chrome_options=options)
        driver.get(l)
        try:
           product = getProductDetails()
           with open("data/productDetails.txt","a+",encoding="utf-8") as f:
               f.write(product.toJSON())
               f.write(",\n")
           print(product.toJSON())
        except Exception as e:
           print("Error: {}".format(e))
        driver.quit()