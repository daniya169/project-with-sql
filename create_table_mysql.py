import mysql.connector
mydb=mysql.connector.connect(host='localhost',
                             port=3325,
                             user='root',
                             password='12345',
                             database='bbd_college1'
                             )

#create cursor object

cur=mydb.cursor()

s='create table info(Sno int(3),Sname varchar(20),Email varchar(20))'

cur.execute(s)
