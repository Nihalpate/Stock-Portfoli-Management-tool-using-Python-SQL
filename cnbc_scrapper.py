# import libraries 
import requests

import requests 
from bs4 import BeautifulSoup

url = "https://www.cnbc.com/quotes/MSFT"

# have to defind the user agent as below otherwise you will ban from the wabsite because website might recognize you as robort
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36"}

page = requests.get(url, headers = headers)
soup = BeautifulSoup(page.content , "html.parser")
soup_1 = BeautifulSoup(soup.prettify(),"html.parser")
body = soup.find("body")

find = soup.find_all("div", class_ = "QuoteStrip-lastPriceStripContainer")
for line in find:
  print(line.find("span").string)
