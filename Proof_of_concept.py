

from attr import attr, attrs
import requests
from bs4 import BeautifulSoup


url = "https://www.bloomberg.com/quote/ANURAS:IN"
url2 = "https://www.google.com/search?q=apple+inc+market+cap&sxsrf=ALiCzsbsXXRFzJmd-9IFXo4LA9zfjYeP2Q:1656277868513&source=lnms&sa=X&ved=2ahUKEwih5oHwg8z4AhUoEVkFHUt3BJgQ_AUoAHoECAEQAg&biw=1280&bih=601&dpr=1.5"

page = requests.get(url)
page2 = requests.get(url2)
#print(page)

soup_1 = BeautifulSoup(page.text, "html.parser")
soup_2 = BeautifulSoup(page2.text, "html.parser")

soup_3 = soup_1.find_all('div',class_ = "overviewRow__66339412a5")

#print(soup_2)
#soup_3 = soup_1.find("fin-streamer",class_= "Fw(b) Fz(36px) Mb(-4px) D(ib)")


# soup_3 = soup_1.find("fin-streamer",{"class":"Fw(b) Fz(36px) Mb(-4px) D(ib)","data-field":"regularMarketPrice",
#                                       "data-pricehint":"2","data-symbol":"TTE","data-test":"qsp-price","data-trend":"none"}).text

print(soup_3)
#soup_4 = soup_2.find_all("div")

#print(soup_4)
