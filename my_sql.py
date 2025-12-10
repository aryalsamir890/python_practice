import mysql.connector as conn

mydb=conn.connect(host="localhost",user="root",password="methane@12345",port=3000)

cursor=mydb.cursor()
cursor.execute("create database if not exists school")
cursor.execute("use school")
cursor.execute("create table if not exists student(name varchar(90),roll int)")
# cursor.execute("select * from student")
# result=cursor.fetchall()
# for i in result:
#     print(i)
#  doing this and using this module make this print(i) be seen while running the main program too