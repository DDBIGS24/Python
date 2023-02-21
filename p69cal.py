while True:
    print("press + for Addition")
    print("press - for Subtraction")
    print("press * for Multiplication")
    print("press / for Divison")
    print("press e for Exit")
    op=input("Enter option =>")
    if op=="+":
        x=int(input("Enter Number =>"))
        y=int(input("Enter NUmber =>"))
        print("Addtion = ",x+y)
    elif op=="-":
        x=int(input("Enter Number =>"))
        y=int(input("Enter NUmber =>"))
        print("Sutraction = ",x-y)
    elif op=="*":
        x=int(input("Enter Number =>"))
        y=int(input("Enter Number =>"))
        print("Multiplication = ",x*y)
    elif op=="/":
        x=int(input("Enter Number =>"))
        y=int(input("Enter Number =>"))
        print("Divison = ",x/y) 
    elif op=="e":
        break
    else:
        print("Option Wrong!!!")                  