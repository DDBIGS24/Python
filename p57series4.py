a=int(input("Enter limit =>"))
s=0
for i in range (1,a+1):
    if i%2==0:
        print(" - ",i,end="")
        s=s-i
    else:
        print(" + ",i,end="")
        s=s+i
print("\n sum= ",s)