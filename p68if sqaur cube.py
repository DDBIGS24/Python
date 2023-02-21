while True:
    print("Press 1 for squar ")
    print("Press 2 for cube ")
    print("Press 3 for Exit ")
    op=int(input("Enter option =>"))
    if op==1:
        x=int(input("Enter Number =>"))
        print("Sqaur = ",x*x)
    elif op==2:
        y=int(input("Enter Number =>"))
        print("Cube = ",y*y*y)
    elif op==3:
        break
    else:
        print("Wrong Option!!!")