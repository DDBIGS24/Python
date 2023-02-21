a=int(input("Enter limit =>"))
s=0
for i in range (1,a+1):
        print(i*i*i," + " ,end="")
        s=s+i
print("\nSum =",s)    