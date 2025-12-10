from emp_payrollsql import mydb,cursor

class employee:
    def __init__(self,name,department):
        self.name=name
        self.department=department
    
    def add_emp(self):
        sql="insert into employee (name,department) values (%s,%s)"
        values=(self.name,self.department)
        cursor.execute(sql,values)
        mydb.commit()


    @staticmethod
    def update_emp():
        ans=input("what do you wanna update::")      
        id=int(input("enter ur employee id ::"))
        if ans=="name":
            name=input("enter the new name:")
            sql="update employee set name=%s where employee_id=%s"
            values=(name,id)
            cursor.execute(sql,values)
            mydb.commit()
        elif ans=="department":
            name=input("enter the new department:")
            sql="update employee set department=%s where employee_id=%s"
            values=(name,id)
            cursor.execute(sql,values)
            mydb.commit()
        else:
            return 
        
    @staticmethod
    def delete_emp():
        id=int(input("enter the id of the employee u wanna delete:"))
        sql="delete from employee where employee_id=%s"
        values=(id,)
        cursor.execute(sql,values)
        mydb.commit()
        return

class salary:
    def __init__(self,bs,allow=None,deduct=None):
        self.basic_salary=bs
        self.allowances=allow
        self.deductions=deduct

    def upload(self):
        id=int(input("enter the employee id::"))
        allowances=0.20*self.basic_salary
        deductions=0.1*self.basic_salary
        ns=self.basic_salary+allowances-deductions
        sql="insert into salary values (%s,%s,%s,%s,%s)"
        values=(id,self.basic_salary,allowances,deductions,ns)
        cursor.execute(sql,values)
        mydb.commit()

    @staticmethod
    def payslip():
        yrname=input("enter yr name please::")
        sql="select e.name,s.basic_salary,s.allowances,s.deductions,s.net_salary from employee as e inner join salary as s on e.employee_id=s.employee_id"
        cursor.execute(sql)
        result=cursor.fetchall()
        for i in result:
            name,basic_salary,allowances,deductions,net_salary=i
            if(name==yrname):
                print(f"your details::\n name:{name}\n basic salary:{basic_salary}\n allowances:{allowances}\n deductions:{deductions}\n net salary={net_salary}")
                return
            
    @staticmethod
    def show_all():
        sql="select e.name,s.basic_salary,s.allowances,s.deductions,s.net_salary from employee as e inner join salary as s on e.employee_id=s.employee_id"
        cursor.execute(sql)
        result=cursor.fetchall()
        for i in result:
            name,basic_salary,allowances,deductions,net_salary=i
            print(f"name:{name}\n basic salary:{basic_salary}\n allowances:{allowances}\n deductions:{deductions}\n net salary={net_salary}")
        return


    @staticmethod
    def update_salary():
        id=int(input("enter the employee id::"))
        sql="update salary set basic_salary=%s where employee_id=%s"
        bs=int(input("enter the new salary"))
        values=(bs,id)   
        cursor.execute(sql,values)
        mydb.commit()


print("1.add employee") 
print("2.update employee") 
print("3. delete employee") 
print("4.upload salary") 
print("5.generate payslip") 
print("6.update salary") 
print("7.show all")
print("8.exit") 


while True:
    val=int(input("choose one option"))
    if val==1:
        ename=input("enter the name")
        dname=input("enter the department")
        o1=employee(ename,dname)
        o1.add_emp()

    elif val==2:
        employee.update_emp()

    elif val==3:
        employee.delete_emp()

    elif val==4:
        bs=int(input("enter the basic salary"))
        o2=salary(bs)
        o2.upload()

    elif val==5:
        salary.payslip()

    elif val==6:
        salary.update_salary()
        
    elif val==7:
        salary.show_all()
    
    else:
        print("exited sucessfully")
        break
        





