

import mysql.connector

dataBase=mysql.connector.connect(
    host='localhost',
    user= 'root',
    passwd= '456SarviKuono'
)
#prepare a cursor object
cursorObject =dataBase.cursor()

#create database
cursorObject.execute("CREATE DATABASE t_hallinta")

print("Valmis!")