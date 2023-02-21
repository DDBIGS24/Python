import random
list1=[]
n=int(input("Enter limit =>"))

for i in range(1,n+1):
    y=random.randint(-20,20)
    list1.append(y)

print(list1)
print(list1.pop(0))
print(list1)
list1.sort()
print(list1)