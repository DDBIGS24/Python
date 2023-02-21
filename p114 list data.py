import random
z=random.randint(1,40)
c=0
y=0

while y!=z:
    y=int(input("Enter guess number =>"))
    c+=1

print("Total tried ",c)