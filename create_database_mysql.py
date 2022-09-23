import mysql.connector
mydb=mysql.connector.connect(host='localhost',
                             port=3325,
                             user='root',
                             password='12345'
                             )

#create cursor object

cur=mydb.cursor()

s='create database bbd_college1'

cur.execute(s)
