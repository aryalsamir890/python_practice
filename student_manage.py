# A small system where you can store student information,
#  update it, and save/retrieve it from a file.

import json

class student:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks

class database(student):
    def add(self):  
        self.student_data={
            "name":self.name,
            "roll":self.roll,
            "marks":self.marks
        }
        f=open("student.json", "r")
        content = f.read()
        f.close()
        if content == "":
            content ='[]'

        data=json.loads(content)
        data.append(self.student_data)
        f = open("student.json", "w")
        f.write(json.dumps(data))
        f.close()

        
    def delete(self,name):
        f=open("student.json","r")
        list=f.read()
        f.close()
        data=json.loads(list)
        for i in data:
            if i["name"]==name:
                data.remove(i)
            break
        f=open("student.json","w")
        list=json.dumps(data)
        f.write(list)
        f.close()

    def search(self,value):
        f=open("student.json","r+")
        list=f.read()
        data=json.loads(list)
        for i in data:
            if i["name"]==value:
                print(i)
                break
        f.close()
            
    def update(self,oname,rname,marks,rollno):
        f=open("student.json","r")   
        val=f.read()
        data=json.loads(val)
        for i in data:
            if i["name"]==oname:
                i["name"]=rname 
                i["marks"]=marks 
                i["roll"]=rollno
                break
        f.close()
        f=open("student.json","w")
        val=json.dumps(data)
        f.write(val)
        f.close()

    def exit(self):
        print("exited sucessfully")

class manager(database):
    def __init__(self):
        print("the app is ready")

    def user_inputs(self):
        self.name=input("enter the name of the student:")
        self.roll=int(input("enter the rollno"))
        self.marks=int(input("enter the marks please!!"))
        super().__init__(self.name,self.roll,self.marks)

    def menu(self):
        print("what actions u do like to perform hmm!!!")
        print("1.add")
        print("2.delete")
        print("3.search")
        print("4.update")
        print("5.exit")
        
        dict={
            "1":self.user_inputs,
            "2":self.delete,
            "3":self.search,
            "4":self.update,
            "5":self.exit
        }
        while True:  # loop runs indefinitely until break
            val = input("choose one!!")
            if val=="1":
                dict[val]()
                self.add()

            elif val=="2":
                name=input("enter the name of student u wanna delete:")
                dict[val](name)
            elif val=="3":
                name=input("enter the name of student u wanna search details:")
                dict[val](name)
            elif val=="4":
                oname=input("enter the  original value u wanna update :")
                rname=input("enter the  replacing name to update ")
                marks=input("enter the  marks to update ")
                rollno=input("enter the  rolllno to update ")
                dict[val](oname,rname,marks,rollno)
            else:
                dict[val]()
                break

obj=manager()
obj.menu()



# 
# 
# 
# by the cht gpts:
import json

# ---------- Student Class ----------
class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

# ---------- Database Class ----------
class Database:
    filename = "students.json"

    def load_data(self):
        with open(self.filename, "r") as f:
            content = f.read()
        return json.loads(content) if content else []

    def save_data(self, data):
        with open(self.filename, "w") as f:
            f.write(json.dumps(data, indent=4))

    def add(self, student):
        data = self.load_data()
        data.append({"name": student.name, "roll": student.roll, "marks": student.marks})
        self.save_data(data)

    def delete(self, name):
        data = self.load_data()
        data = [s for s in data if s["name"] != name]
        self.save_data(data)

    def search(self, name):
        data = self.load_data()
        for s in data:
            if s["name"] == name:
                return s
        return None

    def update(self, name, new_student):
        data = self.load_data()
        for s in data:
            if s["name"] == name:
                s.update({"name": new_student.name, "roll": new_student.roll, "marks": new_student.marks})
                break
        self.save_data(data)

# ---------- Manager Class ----------
class Manager(Database):
    def menu(self):
        while True:
            print("\n--- Student Management ---")
            print("1. Add Student")
            print("2. Delete Student")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                name = input("Name: ")
                roll = int(input("Roll: "))
                marks = int(input("Marks: "))
                self.add(Student(name, roll, marks))
                print("Student added successfully!")

            elif choice == "2":
                name = input("Name to delete: ")
                self.delete(name)
                print("Student deleted successfully!")

            elif choice == "3":
                name = input("Name to search: ")
                student = self.search(name)
                if student:
                    print(student)
                else:
                    print("Student not found.")

            elif choice == "4":
                name = input("Original name to update: ")
                new_name = input("New Name: ")
                roll = int(input("New Roll: "))
                marks = int(input("New Marks: "))
                self.update(name, Student(new_name, roll, marks))
                print("Student updated successfully!")

            elif choice == "5":
                print("Exiting...")
                break

            else:
                print("Invalid choice!")

# ---------- Run the program ----------
if __name__ == "__main__":
    Manager().menu()
