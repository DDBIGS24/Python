print("Press 1 for square")
print("Press 2 for cube")
op=int(input("Enter option =>"))

if op==1:
    y=int(input("Enter no =>"))
    print("Square = ",y*y)
elif op==2:
    y=int(input("Enter no =>"))
    print("Cube = ",y*y*y)
else:
    print("Wrong opt")