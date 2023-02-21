import random
z=random.randint(1,40)
y=0
c=0
while y!=z:
    c+=1
    y=int(input("entrt your guess number"))
    if y<z:
        print("Think greater than that")
    elif y>z:
        print("Think smaller than that")
    else:
        print("z is the correct guess")        