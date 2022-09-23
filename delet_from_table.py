import mysql.connector
mydb=mysql.connector.connect(host='localhost',
                             port=3325,
                             user='root',
                             password='12345',
                             database='bbd_college1'
                             )

#create cursor object

cur=mydb.cursor()

#s="DELETE FROM info WHERE Sname='chetan'"
s='UPDATE info SET Sname="Mohit" WHERE Sno=2'

cur.execute(s)

mydb.commit()
