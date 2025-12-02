

class product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def details(self):
        return({"name":self.name,"price":self.price,"quantity":self.quantity})


class cart:
    def __init__(self):
        self.list = []
        self.sum=0   # initialize once
        
    def add(self):
        name=input("enter the name of the product")
        price=int(input("enter the price "))
        quantity=int(input("enter the quantity"))
        o1=product(name,price,quantity)
        self.list.append(o1.details())

    def remove(self):
        name=input("enter the name to remove ")
        for i in self.list:
            if i["name"]==name:
                self.list.remove(i)
                return

    def total(self):
        for i in self.list:
            self.sum+=i["price"]
        print(f"the total is {self.sum}")

    def __len__(self):
        return len(self.list)
    
    def __str__(self):
        return(f"cart contains:{self.list}")
    

o1=cart()
print("choose the options:")
print("1.add item")
print("2.remove item")
print("3.show item")
print("4.total price ")
print("5.view number  of items")
print("6.exit")

while True:
    val=int(input("enter the choice"))
    if val==1:
        o1.add()
    elif val==2:
        o1.remove()
    elif val==3:
        print(o1)
    elif val==4:
        o1.total()
    elif val==5:
        print(len(o1))
    else:
        print("exited sucessfully!!")
        break


    

    



        


        