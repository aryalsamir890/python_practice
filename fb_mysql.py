import mysql.connector as conn

mydb=conn.connect(host="localhost",
                  user="root",
                  password="methane@12345",
                  port=3000)
cursor=mydb.cursor()
cursor.execute("create database if not exists facebook")
cursor.execute("use facebook")
cursor.execute("create table if not exists users(id int auto_increment primary key ,username varchar(90),email varchar(90),password varchar(90))")
cursor.execute("create table if not exists posts(id int auto_increment primary key, user_id int not null ,title varchar(90),content varchar(90),created_at date,foreign key(user_id) references users(id))")
cursor.execute("create table if not exists comments(id int auto_increment primary key, post_id int ,user_id int not null,comment_text varchar(90), created_at date,foreign key(user_id) references users(id),foreign key(post_id) references posts(id))")
cursor.execute("create table if not exists likes(id int auto_increment primary key,post_id int ,user_id int not null ,created_at date,foreign key(user_id) references users(id),foreign key(post_id) references posts(id))")
