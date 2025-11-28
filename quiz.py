def ques1():
    print("national animal of nepal?")
    print("1.cow 2.buffalo 3.mouse 4.sark")
    ans=int(input("choose the option"))
    return ans 

def ques2():
    print("pm of nepal")
    print("1.modi 2.trump 3.seikh hasina 4.shusila karki")
    ans=int(input("choose the option"))
    return ans
def ques3():
    print("dog is a ?")
    print("1.a gay 2.animal 3.insect 4.madar")
    ans=int(input("choose the option"))
    return ans
def ques4():
    print("this is a ques mo?")
    print(" 1  2  3  4")
    ans=int(input("choose the option"))
    return ans

c=0

print("do you wanna play the game ")
game=input("yes or no?")
if game=="yes":
    ans1=ques1()
    if ans1==1:
        print("correct ans!!")
        c=c+1
    else:
        print("incorrect")
    ans2=ques2()
    if ans2==4:
        print("correct ans!!")
        c=c+1
    else:
        print("incorrect")
    ans3=ques3()
    if ans3==2:
        print("correct ans!!")
        c=c+1
    else:
        print("incorrect")
    ans4=ques4()
    if ans4==4:
        print("correct ans!!")
        c=c+1
    else:
        print("incorrect")
else:
    print("darpog !!")
    
print(f"your total score is:{c}")

