n=int(input("Enter the limit =>"))
s=1
for i in range(n,0,-1):
    print(i,"x",end="")
    s=s*i
print("\nFactorial =",s)
