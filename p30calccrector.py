print("press + for Addition")
print("press - for Subtraction")
print("press * for Multiplication")
print("press / for Divison")
op=input("Enter option =>")

if op=="+":
    x=int(input("Enter no1 =>"))
    y=int(input("Enter no2 =>"))
    print("Addition = ",x+y)
elif op=="-":
    x=int(input("Enter no1 =>"))
    y=int(input("Enter no2 =>"))
    print("Subtraction = ",x-y)
elif op=="*":
    x=int(input("Enter no1 =>"))
    y=int(input("Enter no2 =>"))
    print("Multiplication = ",x*y)
elif op=="/":
    x=int(input("Enter no1 =>"))
    y=int(input("Enter no2 =>"))
    print("Divison = ",x/y)    
else :
     print("Wrong option!!!")    