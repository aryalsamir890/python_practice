import mysql.connector as conn

db=conn.connect(host="localhost",user="root",password="methane@12345",port=3000)

cursor=db.cursor()
cursor.execute("create database if not exists libry")
cursor.execute("use libry")
cursor.execute("create table if not exists books(bookid int,title varchar(90),author varchar(90),total_copies int, available_copies int)")
cursor.execute("create table if not exists transactions(trans_id int auto_increment primary key,book_id int,member_id int,borrow_date date ,return_date date)")
cursor.execute("create table if not exists members(member_id int,name varchar(90),contact int)")

    # Ram borrowed "Python" on 2025-12-09, returned on 2025-12-12

