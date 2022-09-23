import mysql.connector
mydb=mysql.connector.connect(host='localhost',port=3325,user='root',password='12345')
print(mydb.connection_id)
