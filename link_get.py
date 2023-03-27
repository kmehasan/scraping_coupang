from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
link = "https://www.coupang.com/np/categories/176522?listSize=60&brand=&offerCondition=&filterType=rocket_wow%2Ccoupang_global&isPriceRange=false&minPrice=&maxPrice=&page={}&channel=user&fromComponent=N&selectedPlpKeepFilter=&sorter=bestAsc&filter=&rating=0&rocketAll=true"
options = webdriver.ChromeOptions()
prefs = {
  "translate_whitelists": {"ko":"en"},
  "translate":{"enabled":"true"}
}
options.add_experimental_option("prefs", prefs)
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'
options.add_argument('user-agent={0}'.format(user_agent))

links = []
for i in range(1,5):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),chrome_options=options)  # Optional argument, if not specified will search path.
    driver.get(link.format(i))
    for l in driver.find_elements(By.XPATH,"//*[@class='baby-product-link']"):
        links.append(l.get_attribute("href"))
    driver.quit()
with open("data/links.txt","w") as f:
    for l in links:
        f.write(l + "\n")




