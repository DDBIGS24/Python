import random
n=5
c=0
c1 = 0
for i in range(1,n+1):
    x=random.randint(1,50)
    y=random.randint(1,50)
    print("No1 = ",x," No2 = ",y)
    z=int(input("Add Number =>"))
    a = x+y
    if z == a:
        c+=1
    else:
        c1 += 1

print("Total Matched = ",c)

print("Total Didn't Matched = ",c1)    

        