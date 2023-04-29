from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from model.product import Product
import zlib
from fake_useragent import UserAgent

item_ids = []
trying_item_id = 0
ua = UserAgent()
# proxy = '2.56.119.93:5074'
def getProductDetails():
    name = driver.find_element(By.XPATH,"//*[@class='prod-buy-header__title']").get_attribute("innerText")
    nameKo = driver.find_element(By.XPATH,"//*[@class='prod-share__twitter']").get_attribute("data-title")
    price_after_dc = driver.find_element(By.XPATH,"//*[@class='total-price']").get_attribute("innerText")
    thumbs = [img.get_attribute('src') for img in driver.find_elements(By.XPATH,"//*[@class='prod-image__items']//img")]
    mainImages = [img.get_attribute('src') for img in driver.find_elements(By.XPATH,"//*[@class='subType-IMAGE']//img")]
    category2 = driver.find_element(By.XPATH,"//*[@id='breadcrumb']").get_attribute("innerText").replace("\n"," ")
    category2 = " > ".join([i.strip() for i in category2.split(">")])
    category = category2.split(">")[2].strip()
    brand = driver.find_element(By.XPATH,"//*[@class='prod-brand-name']").get_attribute("innerText")
    brandKo = driver.find_element(By.XPATH,"//*[@class='prod-brand-name']").get_attribute("data-brand-name")

    try:
       capacity = driver.find_element(By.XPATH,"//*[@class='prod-option__selected-container']").get_attribute("innerText").replace("\n"," ")
    except:
       capacity = ""
    capacity2 = driver.find_element(By.XPATH,'//*[@id="itemBrief"]/div/table/tbody/tr[1]/td[1]').get_attribute("innerText").replace("\n"," ")
    full_description = driver.find_element(By.XPATH,"//*[@id='itemBrief']").get_attribute('innerHTML')
    descAll = driver.find_elements(By.XPATH,"//*[@class='prod-description-attribute']//li")
    desc = "\n".join([li.get_attribute("innerText") for li in descAll[1:-1]])
    CoupangProductNumber = descAll[-1].get_attribute("innerText").split(":")[1].strip()
    KeySpecifications = driver.find_element(By.XPATH,'//*[@id="itemBrief"]/div/table/tbody/tr[1]/td[2]').get_attribute("innerText").replace("\n"," ")
    textBetween = ""
    
    try:
      price_before_dc = driver.find_element(By.XPATH,"//*[@class='origin-price']").get_attribute("innerText")
    except:
      price_before_dc = "No discount"
    product = Product(name,nameKo,price_before_dc,price_after_dc,category,category2,brand,brandKo,thumbs,mainImages,capacity,capacity2,desc,CoupangProductNumber,KeySpecifications,textBetween,l,full_description)
    product = product.translate()
    
    print()
    print(name,nameKo,price_after_dc,price_before_dc)
    print()
    return product

def getFromLink(link):
  global driver
  global l
  global trying_item_id
  l = link
  trying_item_id = int(link.split("?")[0].split("/")[-1])

  # Check if already scaraed
  if trying_item_id in item_ids:
     print("Already scraped")
     return
  userAgent = ua.random
  options = webdriver.ChromeOptions()
  # user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'
  # options.add_argument('user-agent={0}'.format(user_agent))
  # options.add_argument("--headless")
  options.add_argument('--disable-gpu')
  options.add_argument('--no-sandbox')
  # options.add_argument('--proxy-server=%s' % proxy)
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_experimental_option('useAutomationExtension', False)

  user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
  options.add_argument('user-agent={0}'.format(userAgent))
  driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),chrome_options=options)
  driver.get(link)
  # sleep(5)
  try:
    # save full html data
    with open(f"data/html_data/{trying_item_id}.txt","wb") as f:
        f.write(zlib.compress(driver.page_source.encode()))
    # Get product details
    product = getProductDetails()

    # Save product details
    with open("data/productDetailsdelete.txt","a+",encoding="utf-8") as f:
        f.write(product.toJSON())
        f.write(",\n")
    print(product.toJSON())
    item_ids.append(trying_item_id)

    # Save item ids
    with open("data/link_info/item_ids.txt","a+") as f:
        f.write(str(trying_item_id))
        f.write("\n")
    
    # Save done links
    with open("data/link_info/done.txt","a+") as f:
        f.write(link)
        f.write("\n")
  except Exception as e:
    # Save failed links
    with open("data/link_info/failed.txt","a+") as f:
        f.write(link)
        f.write("\n")
    print("Error: {}".format(e))
  driver.quit()

def main():
  global item_ids
  error_link = []
  with open("data/link_info/item_ids.txt","r") as f:
      item_ids = f.readlines()
      item_ids = [int(i.strip().replace("\n","")) for i in item_ids]
  with open("data/link_info/failed.txt","r") as f:
      error_link = f.readlines()
      error_link = [i.strip().replace("\n","") for i in error_link]
  with open("data/links.txt","r") as f:
      links = f.readlines()
      for l in links:
          if l.strip().replace("\n","") not in error_link:
            getFromLink(l.strip().replace("\n",""))

if __name__ == "__main__":
    main()
    # getFromLink("https://www.coupang.com/vp/products/5796999144?itemId=9930394993&vendorItemId=77213650808&sourceType=CATEGORY&categoryId=176644&isAddedCart=")
