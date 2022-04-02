import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", passwd="Sh@ile$h.29", database="jdbc_db")

mycursor = conn.cursor()
mycursor.execute("select * from students")

for i in mycursor:
    print(i)