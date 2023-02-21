n=int(input("Enter the limit =>"))
c=0
s=0
for i in range(1,n+1):
    if i % 7 ==0:
        c+=1
        s+=i
        print(i)
print("sum = ",s," count = ",c)