a=int(input("enter a number :"))
b=int(input("enter another number:"))
print("what operation u do like to perfom::")
print("1.+")
print("2.-")
print("3.*")
print("4./")
value=int(input("choose and give the ans "))
match value:
    case 1:
        print(a+b)
    case 2:
        print(a-b)
    case 3:
        print(a*b)
    case 4:
        print(a/b)
    case _:#this is the default case 
        print("Invalid choice")

# by chatgpt
# Simple calculator using a dictionary

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

# Dictionary that maps symbols to functions
operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div
}

# Take inputs
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Ask which operation
op = input("Enter operation (+, -, *, /): ")

# Perform and print result
if op in operations:
    result = operations[op](a, b)   # calls the correct function
    print("Result:", result)
else:
    print("Invalid operation!")
