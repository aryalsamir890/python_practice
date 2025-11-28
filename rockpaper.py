# rock ,paper and scissors game using the dictionery method  !!
import random

choices=["rock","paper","scissors"]

# the winning rules are set in the dictionery like rock beats scissors 
dictionery={
    "rock":"scissors",                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    "paper":"rock",
    "scissors":"paper"
}
user=input("choose any one among the rock,paper and the scissors!!").lower()
if user not in choices:
    print("invalid choice!!!")
else:
    computer=random.choice(choices)
    print(computer)
    if(user==computer):
        print("tie happened")
# this down thing is the main logic 
# look if  dictionery["rock"] == computer(means computer input value )
# that is "scissors" == "scissors"  → True(user wins )
# means look if value of key matches the computer  input means the user wins else computer wins 
    elif(dictionery[user]==computer):
        print("user wins")
    else:
        print("computer wins ")




# #simple code by me using if else!! 
# import random 

# choices=["rock","paper","scissors"]
# i=0
# j=0

# for k in range(5):
#     val=random.choice(choices)
#     print(val)
#     user=input("choose one among R,P and scissors: ")
#     if(val=="rock" and user=="paper"):
#         print("user wins")
#         i=i+1
#     elif(val=="paper" and user=="scissors"):
#         print("user wins ")
#         i=i+1
#     elif(val=="scissors" and user=="rock"):
#         print("user wins")
#         i=i+1
#     elif(val=="scissors" and user=="paper"):
#         print("computer wins")
#         j=j+1
#     elif(val=="paper" and user=="rock"):
#         print("computer wins")
#         j=j+1
#     elif(val=="rock" and user=="scissors"):
#         print("computer wins")
#         j=j+1
#     else:
#         print("tie happened try again please!!!")

# if(i>j):
#     print("user wins")
# else:
#     print("computer wins")