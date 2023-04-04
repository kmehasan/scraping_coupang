from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import os

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
root_path = "data"
category = "Skin Care"
sub_category = "Mist"

sub_category_path = f'{root_path}/{category}/{sub_category}'
subcategoryExists = os.path.exists(sub_category_path)

if not subcategoryExists:
   os.makedirs(sub_category_path)
   print("The new directory is created!")

link = "https://www.coupang.com/np/categories/486251?listSize=120&brand=&offerCondition=&filterType=rocket%2Crocket_wow%2Ccoupang_global&isPriceRange=false&minPrice=&maxPrice=&page={}&channel=user&fromComponent=Y&selectedPlpKeepFilter=&sorter=bestAsc&filter=&component=486151&rating=0&rocketAll=true"
options = webdriver.ChromeOptions()
prefs = {
  "translate_whitelists": {"ko":"en"},
  "translate":{"enabled":"true"}
}
options.add_experimental_option("prefs", prefs)
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'
options.add_argument('user-agent={0}'.format(user_agent))

links = []
for i in range(1,10):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),chrome_options=options)  # Optional argument, if not specified will search path.
    driver.get(link.format(i))
    for l in driver.find_elements(By.XPATH,"//*[@class='baby-product-link']"):
        if l not in links:
            links.append(l.get_attribute("href"))
    driver.quit()
with open(f"{sub_category_path}/links.txt","w") as f:
    for l in links:
        f.write(l + "\n")




