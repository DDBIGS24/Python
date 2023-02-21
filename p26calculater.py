print("press 1 for Addition")
print("press 2 for Subtraction")
print("press 3 for Multiplication")
print("press 4 for Divison")
op=int(input("Enter option =>"))

if op==1:
    x=int(input("Enter no1 =>"))
    y=int(input("Enter no2 =>"))
    print("Addition = ",x+y)
elif op==2:
    x=int(input("Enter no1 =>"))
    y=int(input("Enter no =>"))
    print("Subratiction = ",x-y)
elif op == 3:
    x=int(input("Enter no1 =>"))
    y=int(input("Enter no2 =>"))
    print("Multiplication = ",x*y)
elif op == 4:
    x=int(input("Enter no1 =>"))
    y=int(input("Enter no2 =>"))
    print("Multiplication = ",x/y)
else:
    print("Wrong option!!!")