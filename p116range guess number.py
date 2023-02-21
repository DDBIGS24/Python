import random
z=random.randint(1,40)
y=0
s=1
en=40
c=0
while y!=z:
    print("Your range is",s,"And",en)
    c+=1
    y=int(input("entrt your guess number"))
    if y<z:
        print("Think greater than that")
    elif y>z:
        print("Think smaller than that")
    else:
        print("Your guess is right") 
print("You tried",c,"times")               