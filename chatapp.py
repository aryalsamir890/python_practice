import datetime 

class user:
    def __init__(self,name,username):
        self.name=name
        self.username=username

class message:
    def __init__(self,obj):
        self.id=0
        self.obj=obj

    def msg(self):
        text=input("enter the msg to sent ::")
        x=datetime.date.today()
        self.id+=1
        data={"name":self.obj.name,"username":self.obj.username,"text":text,"date":x,"id":self.id}
        return data


class chat:
    def __init__(self,obj):
        self.list=[]
        self.obj=obj

    def sentmsg(self):
        self.list.append(self.obj.msg())

    def delete(self):
        print(self.list)
        id=int(input("enter the id of the msg you wanna delete!!"))
        for i in self.list:
            if i["id"]==id:
                self.list.remove(i)
                print("deleted sucessfully!!")
                return
            
    def show(self):
        print(self.list)

obj=None
obj1=None
obj2=None
print("choose the action::")
print("1.your details")
print("2.sent message")
print("3.delete message ")
print("4.show all")
print("exit ")

while True:
    val =int(input("enter the option\t"))
    if val==1:
        name=input("enter the name !!")
        username=input("enter the username")
        obj=user(name,username)
        obj1=message(obj)
        obj2=chat(obj1)

    elif val==2:
        obj2.sentmsg()

    elif val==3:
        obj2.delete()

    elif val==4:
        obj2.show()

    else:
        print("exited sucessfully")
        break