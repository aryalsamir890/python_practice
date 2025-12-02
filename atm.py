
class account:
    def __init__(self):
        self.__pin=9845
        self.__balance=5000
    
    def details(self):
        return self.__pin


    def balance(self):
        # pin=int(input("do enter your pin to check the balance :"))
        # if pin==self.__pin:
        print(f"your balance is{self.__balance}")

    def deposit(self):
        amt=int(input("enter the amt to deposit ::"))
        self.__balance=self.__balance+amt

    def withdraw(self):
        amt=int(input("enter the amt to withdraw ::"))
        if self.__balance>amt:
            self.__balance=self.__balance-amt
        else:
            print("not sufficient amt ")

class atm:
    def pin(self):
        pin=int(input("enter the pin ::"))
        o1=account()
        val=o1.details()
        if val==pin:
            print("pin verified sucessfully")
            self.menu(o1)
        else:
            print("pin not verified !!")
            return
        
    def menu(self,object):
        print("listed actions")
        print("1.balance")
        print("2.deposit")
        print("3.withdraw")
        print("4.exit")
        while True:
            val=int(input("choose any action::"))

            if val==1:
                object.balance()

            elif val==2:
                object.deposit()
            
            elif val==3:
                object.withdraw()

            else:
                print("exit")
                break

obj=atm()
obj.pin()

        
        

