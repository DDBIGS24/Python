no=int(input("Enter the Number =>"))
c1=0
s1=0
c2=0
s2=0
for i in range(1,no+1):
    if i%2==0:
        print(i , "is Even")
        c1+=1
        s1+=i
    else:
        print(i,"is odd")        
        c2+=1
        s2+=i
print("Even count = ",c1,"Even sum = ",s1)
print("odd count = ",c2,"odd sum = ",s2)    