n=int(input("Enter Number =>"))
b=int(input("Enter Limit =>"))
c=0
s=0
for i in range(1,b+1):
    if i % n ==0:
        c+=1
        s+=i
        print(i)
print("Sum = ",s," Count = ",c) 

"""
1 is odd
2 is even

even count and sum
odd count and sum


7%

count
sum
"""