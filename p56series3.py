a=int(input("Enter limit =>"))
s=0
for i in range (1,a+1):
        if i%2==0:
          print(i*i," + " ,end="")
          s=s+i*i
        else:
                print(i*i*i," + " ,end="")
                s=s+i*i*i
        
print("\n sum=",s)