from requests_html import HTMLSession

session = HTMLSession()

from bs4 import BeautifulSoup as bs
import urllib.request

url = "https://www.coupang.com/vp/products/6964520622?itemId=16967413502&vendorItemId=84144315193&sourceType=CATEGORY&categoryId=176422"
header = { 
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", 
	"Accept-Encoding": "gzip, deflate, br", 
	"Accept-Language": "en-US,en;q=0.5", 
	"Sec-Fetch-Dest": "document", 
	"Sec-Fetch-Mode": "navigate", 
	"Sec-Fetch-Site": "none", 
	"Sec-Fetch-User": "?1", 
	"Upgrade-Insecure-Requests": "1", 
	"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0" 
}
# request and grab content
print("starting request..."+url)
proxy = "http://103.197.251.202:80"
r = session.get(url,headers=header)

r.html.render()  # this call executes the js in the page

# data = r.html #requests.get(url,headers=header).content
# req = urllib.request.Request(url,headers= header)
# with urllib.request.urlopen(req) as response:
#     data = response.read()
print("request done")
# print(data)
soup = r.html.html #bs(data, 'html.parser')
print("soup done")
print(soup)
with open("test2.html", "w",encoding='utf-8') as f:
    f.write(str(soup))