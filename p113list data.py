import random
print("press + for Addition")
print("press - for Subtraction")
print("press * for Multiplication")
print("press / for Divison")
print("press e for exit")
op=input("Enter option =>")
c1=0
c2=0
if op=="+":
        for i in range(1,6):
            x=random.randint(1,50)
            y=random.randint(1,50)
            print("No1 = ",x," No2 = ",y)
            z=int(input("Addtion Number =>"))
            a = x+y
            if z == a:
                c1+=1
            else:
                c2 += 1
        print("Right answers are ",c1, " Wrong answers are ",c2)
elif op=="-":
        for i in range(1,6):
            x=random.randint(1,50)
            y=random.randint(1,50)
            print("No1 = ",x,"No2 = ",y)
            z=int(input("Subtraction Number =>"))
            a = x-y
            if z == a:
                c1+=1
            else:
                c2 += 1
        print("Right answers are ",c1, " Wrong answers are ",c2)        
elif op=="*":
        for i in range(1,6):
            x=random.randint(1,50)
            y=random.randint(1,50)
            print("No1 = ",x,"No2 = ",y)
            z=int(input("Multiplication Number => "))
            a = x*y
            if z == a:
                c1+=1
            else:
                c2 += 1
        print("Right answers are ",c1, " Wrong answers are ",c2)        
elif op=="/":
        for i in range(1,6):
            x=random.randint(1,50)
            y=random.randint(1,50)
            print("No1 = ",x,"No2 = ",y)
            z=int(input("Divison Number =>"))
            a = x/y
            if z == a:
                c1+=1
            else:
                c2 += 1
        print("Right answers are ",c1, " Wrong answers are ",c2)        
elif op == "e":
        print("Goodbye...")
else:
        print("wrong option!!!")       