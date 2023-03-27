from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
prefs = {
  "translate_whitelists": {"ko":"en"},
  "translate":{"enabled":True}
}
options.add_experimental_option("prefs", prefs)
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
    price = driver.find_element(By.XPATH,"//*[@class='total-price']").get_attribute("innerText")
with open("data/links.txt","r") as f:
    links = f.readlines()
    for l in links:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),chrome_options=options)
        sleep(15)
        driver.get(l)
        name = driver.find_element(By.XPATH,"//*[@class='prod-buy-header__title']").get_attribute("innerText")
        nameKo = driver.title
        price_after_dc = driver.find_element(By.XPATH,"//*[@class='total-price']").get_attribute("innerText")
        price_before_dc = driver.find_element(By.XPATH,"//*[@class='origin-price']").get_attribute("innerText")
        print()
        print(name,nameKo,price_after_dc,price_before_dc)
        print()
        driver.quit()