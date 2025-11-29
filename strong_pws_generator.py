import random
import string 

pool=string.digits + string.ascii_letters + string.punctuation
req=int(input("enter the length of the pws u wanna create"))
data=random.choices(pool,k=req)
string="".join(data)
print(f"the strong pws is {string}")


