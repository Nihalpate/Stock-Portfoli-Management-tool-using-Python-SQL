import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Nihal@301197",
    database = "nihal"
 )

#nihal = mydb.cursor()
#nihal.execute()

file = open("q_1.sql","r")
for i in file:
    print(i)