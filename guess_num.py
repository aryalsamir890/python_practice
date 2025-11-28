# number guessing game in python
# written by me
import random 

number=random.randint(1,50)
print(number)
guess=int(input("enter a +ve number::"))

def try_again():
    if(guess>number):
        if(guess-number>10 ):
           print("too far")
        elif(guess-number<10) :
            print("too close ")
    else:
        if(number-guess>10):
            print("too far")
        elif(number-guess<10):
            print("too close")
    

for i in range(10):
    if(guess==number):
        print("you have guessed the correct number !!")
        break
    else:
        # guess=int(input("enter a new +ve number::"))
        try_again()
        guess=int(input("enter a +ve number::"))


# by chatgpt more advanced and the less line consumed code 
import random

number = random.randint(1, 50)

def try_again(guess, number):
    diff = abs(guess - number)
    if diff > 10:
        print("Too far!")
    else:
        print("Too close!")

for i in range(10):
    guess = int(input("Enter a +ve number: "))
    if guess == number:
        print(f"🎉 Congratulations! You guessed it in {i+1} tries.")
        break
    try_again(guess, number)  # now it runs for every guess
else:
    print(f"Sorry! The number was {number}.")


        