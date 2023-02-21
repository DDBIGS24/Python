import random
x=random.randint(1,50)
y=random.randint(1,50)
print("No1 = ",x," No2 = ",y)
z=int(input("Add Number =>"))
a = x+y
if z == a:
    print("Matched")
else:
    print("Didn't match...")