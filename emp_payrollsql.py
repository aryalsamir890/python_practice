import mysql.connector as conn

mydb=conn.connect(host="localhost",
                  user="root",
                  password="methane@12345",
                  port=3000)
cursor=mydb.cursor()
cursor.execute("create database if not exists company")
cursor.execute("use company")
cursor.execute("create table if not exists employee(employee_id int auto_increment primary key,name varchar(90),department varchar(90))")
cursor.execute("create table if not exists salary(employee_id int,basic_salary int,allowances int ,deductions int,net_salary int)")
