import mysql.connector
mydb=mysql.connector.connect(host='localhost',
                             port=3325,
                             user='root',
                             password='12345',
                             database='bbd_college1'
                             )

#create cursor object

cur=mydb.cursor()

s='insert into info(Sno,Sname,Email) value(%s,%s,%s)'

#b1=(1,'chetan','xyz@gmail.com')
b2=(2,'Anuj','sdf@gamil.com')

cur.execute(s,b2)

mydb.commit()
