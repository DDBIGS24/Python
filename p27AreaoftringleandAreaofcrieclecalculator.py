print("press 1 for Area of triangle")
print("press 2 for Area of circle")
op=int(input("Enter option =>"))

if op==1:
    h=int(input("Enter Height =>"))
    b=int(input("Enter Base =>"))
    print("Area of tringle = ",h*b*0.5)
elif op==2:
    r=int(input("Enter Radius =>"))
    print("Area of circle = ",r*r*3.14)   
else:
    print("Wrong option!!!")      