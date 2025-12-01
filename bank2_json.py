import json
import string
import random

class account:
    def __init__(self):
        self.__name = ""

    def fill(self,name,accnum,amount):
        self.__name=name
        self.__accnum=accnum#new user create 
        self.__balance=amount


    def read(self):
        f=open("bank2.json","r")
        data=f.read()
        f.close()
        if data =="":
            return []
        else:
            return json.loads(data)
        
    def write(self,content):
        val=self.read()
        f=open("bank2.json","w")
        val.append(content)
        data=json.dumps(val)
        f.write(data)
        f.close()

    def user(self):
        data={
            "name":self.__name,
            "accnum":self.__accnum,
            "balance":self.__balance
        }
        val=self.checkuser(self.__name)
        if val ==1:
            return
        else:
            self.write(data) 

    def checkuser(self,name):
        data=self.read()
        for i in data:
            if i["name"]==name:
                print("your account already exists:")
                return 1
        

    def deposit(self):
        amt=int(input("enter the amt to deposit:"))
        data=self.read()
        if self.__name!="":
            name=self.__name
        else:
            name=input("enter ur name please!!")

        for i in data:
            if i["name"]==name:
                balance=i["balance"]
                i["balance"]=balance+amt
                f=open("bank2.json","w")
                val=json.dumps(data)
                f.write(val)
                f.close()
                return
        print("no user found!!")


    def withdraw(self):
        value=int(input("enter the amt to withdraw"))
        data=self.read()
        if self.__name!="":
            name=self.__name
        else:
            name=input("enter ur name please!!")
        for i in data:
            if i["name"]==name:
                balance=i["balance"]
                if balance>value:
                    i["balance"]=balance-value
                    print(f"Rs.{value}is withdrawn sucessfully!")
                    f=open("bank2.json","w")
                    val=json.dumps(data)
                    f.write(val)
                    f.close()
                    return
                else:
                    print("insufficient money !!")
                return    
        print("user not found")

    def checkbalance(self):
        data=self.read()
        if self.__name!="":
            name=self.__name
        else:
            name=input("enter ur name please!!")
        for i in data:
            if i["name"]==name:
                print(f"your balance is :{i["balance"]}")
                return 
        print("user not found!!")
    
print("welcome to samir's bank")
print("choose any actions to perform :")
print("1.create account.")
print("2.deposit money")
print("3.withdraw money ")
print("4.check balance ")
print("5.exit+ \n")


obj1=account()

while True:
    val=input("enter the choice:\t")
    if val=="1":
        name=input("enter ur name:\t")
        pool=string.digits
        accnum="".join(random.choices(pool,k=10))
        balance=int(input("you must deposit 1000 to open account:\t"))
        obj1.fill(name,accnum,balance)
        obj1.user()

    elif val=="2":
        obj1.deposit()

    elif val=="3":
        obj1.withdraw()

    elif val=="4":
        obj1.checkbalance()

    else:
        print("thanks for visiting!!")
        break

