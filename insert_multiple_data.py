import mysql.connector
mydb=mysql.connector.connect(host='localhost',
                             port=3325,
                             user='root',
                             password='12345',
                             database='bbd_college1'
                             )

#create cursor object

cur=mydb.cursor()

#how to insret multiple data to table

s='insert into info(Sno,Sname,Email) value(%s,%s,%s)'
info1=[(1,'chetan','xyz@gmail.com'),(3,'Anuj','sdf@gmail.com')]

cur.executemany(s,info1)

mydb.commit()
