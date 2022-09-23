import mysql.connector
mydb=mysql.connector.connect(host='localhost',
                             port=3325,
                             user='root',
                             password='12345',
                             database='bbd_college1'
                             )

#create cursor object

cur=mydb.cursor()

s='select * from info'

cur.execute(s)

Result=cur.fetchall()

for rec in Result:
    print(rec)
