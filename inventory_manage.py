
import json


class product:
    def __init__(self,name,price,quantity,productid):
        self.name=name
        self.price=price
        self.quantity=quantity
        self.productid=productid

    def details(self):
        return({
            "name":self.name,
            "price":self.price,
            "quantity":self.quantity,
            "id":self.productid
            })

class inventory:
    def add(self):
        name=input("name of product:")
        price=int(input("price of product:"))
        quantity=int(input("quantity of product:"))
        productid=int(input("id of product:"))
        obj1=product(name,price,quantity,productid)
        data=self.read()
        data.append(obj1.details())
        self.write(data)
        

    def read(self):
        with open("inventory.json","r") as f :
            data=f.read()
            if data =="":
                return []
            else:
                return json.loads(data)
            
    def write(self,content):
        with open("inventory.json","w") as f :
            data=json.dumps(content)
            f.write(data)

    def update(self):
        data=self.read()
        name=input("enter the name of the product to update its quantity!")
        reset=int(input("enter the new quantity value"))
        for i in data:
            if i["name"]==name:
                i["quantity"]=reset
                self.write(data)
                return
            
    def delete(self):
        data=self.read()
        name=input("enter the name of the product to delete !")
        for i in data:
            if i["name"]==name:
                data.remove(i)
                self.write(data)
                return
            
o1=inventory()
print("choose the actions u do wanna perform in the inventory haha !!!")
print("1.add product")
print("2.update product")
print("3.delete product")
print("4.exit")

while True:
    val=int(input("choose the option please::"))
    if val==1:
        o1.add()

    elif val==2:
        o1.update()

    elif val==3:
        o1.delete()
    else:
        break
        