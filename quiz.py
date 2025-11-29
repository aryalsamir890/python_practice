# code given by the chatgpt haha!!
questions = [
    {
        "question": "1. What is the capital of Nepal?",
        "options": ["A) Pokhara", "B) Kathmandu", "C) Bhaktapur"],
        "answer": "B"
    },
    {
        "question": "2. Who developed Python?",
        "options": ["A) Steve Jobs", "B) Mark Zuckerberg", "C) Guido van Rossum"],
        "answer": "C"
    },
    {
        "question": "3. Which one is a programming language?",
        "options": ["A) Python", "B) HTML", "C) Both"],
        "answer": "C"
    }
]

score = 0

print("\n===== QUIZ GAME =====\n")

for q in questions:
    print(q["question"])
    for opt in q["options"]:
        print(opt)
    
    user_ans = input("Your answer (A/B/C): ").strip().upper()

    if user_ans == q["answer"]:
        print("✔ Correct!\n")
        score += 1
    else:
        print("✘ Wrong!\n")

print(f"Your final score: {score}/{len(questions)}")

# code by me :
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
if(c==4):
    print("topper")

else:
    print("study hard bro!!")

