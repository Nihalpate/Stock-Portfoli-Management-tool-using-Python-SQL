
# importing connection file
from mysql.connector import connection
import pandas as pd
import requests
from bs4 import BeautifulSoup


# connecting python to the SQL database 
# mydb = connection.MySQLConnection(
#     host= "localhost", 
#     user ="root",
#     database = "nihal",
#     password ="Nihal@301197"
#     )

# # exicuting query 
# cursor = mydb.cursor()
# query = "C:\nihal\Data Analyest Portfolio\q_1"
# cursor.execute(query)
# for line in cursor:
#     print(line)


# file = open("q_1.sql", "r")
# rfile = file.read()
# file.close()

# # exicuting query 
# cursor = mydb.cursor()
# query = rfile
# cursor.execute(query)
 
# df = pd.DataFrame(cursor)
# print(df)
url = "https://finance.yahoo.com/quote/AAPL/"

page = requests.get(url)
#print(page)

soup_1 = BeautifulSoup(page.text, "html.parser")

#print(soup_2)
soup_3 = soup_1.find("fin-streamer",{"class":"Fw(b) Fz(36px) Mb(-4px) D(ib)","data-field":"regularMarketPrice",
                                     "data-pricehint":"2","data-symbol":"AAPL","data-test":"qsp-price","data-trend":"none"}).text

print(soup_3)