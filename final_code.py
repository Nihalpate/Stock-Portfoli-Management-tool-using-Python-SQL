

from dbm import _Database
from venv import create
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Nihal@301197"
 )



def scrapper(company_code):
    #company_name = input("Enter the company code")

    # import libraries 

    import requests 
    from bs4 import BeautifulSoup
    import time 
    from datetime import datetime

    url = "https://www.cnbc.com/quotes/"+ " " + company_code 
    now =  datetime.now()

    # have to defind the user agent as below otherwise you will ban from the wabsite because website might recognize you as robort
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36"}

    page = requests.get(url, headers = headers)
    soup = BeautifulSoup(page.content , "html.parser")
    soup_1 = BeautifulSoup(soup.prettify(),"html.parser")
    body = soup.find("body")

    find = soup.find_all("div", class_ = "QuoteStrip-lastPriceStripContainer")
    find_1 = soup.find_all("div", class_ = "QuoteStrip-quoteStripSubHeader")
    find_3 = soup.find("span", class_ = "QuoteStrip-name").string
    
    company_name = find_3
    
    for line in find:
        stake_price = line.find("span").string
        
    for line_1 in find_1:
        currncy = line_1.find_all("span")
        for line in currncy:
            sing = (line.get_text())
    return stake_price, sing, now


company_code = input("Enter The company Name")
scrapper(company_code)

nihal = mydb.cursor()
nihal.execute("USE nihal")