import mysql.connector as conn

mydb=conn.connect(host="localhost",
                  user="root",
                  password="methane@12345",
                  port=3000)

cursor=mydb.cursor()
cursor.execute("create database if not exists cghall")
cursor.execute("use cghall")
cursor.execute("create table if not exists movies(id int auto_increment primary key,name varchar(90) not null,duration time,genre varchar(90))")
cursor.execute("create table if not exists shows(id int auto_increment primary key,name varchar(90),show_time timestamp,movid int not null,foreign key(movid) references movies(id))")
cursor.execute("create table if not exists seats(id int auto_increment primary key,status int,movid int ,showid int,foreign key(showid) references shows(id),foreign key(movid) references movies(id))")
# cursor.execute("drop database cghall")
