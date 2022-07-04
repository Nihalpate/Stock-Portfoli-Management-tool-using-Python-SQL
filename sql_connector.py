from sympy import re


def sql_runner (file_name):

    import mysql.connector
    from pathlib import Path

    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Nihal@301197",
        database = "nihal"
    )
    # to find the relative path for perticular filename in the current directory
    filepath = Path(__file__).parent / file_name
    print("file path: " + str(filepath))
    filename = open(filepath)
    text = (filename.read())

    nihal = mydb.cursor()
    nihal.execute(text + "tableau_table_4")

    for i  in nihal:
        print(i)



sql_runner("q_1.sql")