from my_sql import mydb,cursor

def add_student():
    sql="insert into student (name,roll) values(%s,%s)"
    name=input("enter the name::")
    roll=int(input("enter your rollnumber please::")) 
    values=(name,roll)
    cursor.execute(sql,values)
    mydb.commit()
    return
    # this is the much better way to do to prevent from the sql injection!!

def view_student():
    sql="select * from student"
    cursor.execute(sql)
    result=cursor.fetchall()
    for i in result:
        print(i)
    return

def update_student():
    val=input("what do you want to change name or the roll")
    if val=="name":
        sql="update student set name=%s where roll=%s"
        name=input("do enter the new name")
        roll=int(input("enter the rollno"))
        value=(name,roll)
        cursor.execute(sql,value)
    elif val=="roll":
        sql="update student set roll=%s where name=%s"
        name=input("do enter the name ")
        roll=int(input("enter the newroll"))
        value=(roll,name)
        cursor.execute(sql,value)
    else:
        print("invalid choice:")
    mydb.commit()
    return

def delete_student():
    value=(input("enter the roll number u wanna delete"),)
    sql="delete from student where roll=%s"
    cursor.execute(sql,value)
    mydb.commit()
    return

print("1.add ")
print("2.view ")
print("3.update ")
print("4.delete ")

while True:
    val=int(input("choodse the option:"))
    if val==1:
        add_student()
    elif val==2:
        view_student()
    elif val==3:
        update_student()
    elif val==4:
        delete_student()
    else:
        print("exited sucessfully")
        break





    
