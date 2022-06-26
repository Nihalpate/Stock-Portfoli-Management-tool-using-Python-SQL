

import requests
from bs4 import BeautifulSoup


url = "https://finance.yahoo.com/quote/AAPL/"

page = requests.get(url)
#print(page)

soup_1 = BeautifulSoup(page.text, "html.parser")

#print(soup_2)
soup_3 = soup_1.find("fin-streamer",{"class":"Fw(b) Fz(36px) Mb(-4px) D(ib)","data-field":"regularMarketPrice",
                                     "data-pricehint":"2","data-symbol":"AAPL","data-test":"qsp-price","data-trend":"none"}).text

print(soup_3)