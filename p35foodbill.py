print("press d for dhosa(300)")
print("press m for maggie(100)")
print("press s for sandwhich(200)")
print("press p for panjabi dish(300)")
print("press g for gujarati dish(200)")
op=input("Enter option =>")

if op=="d":
    d=int(input("Enter quantity of dhosa =>"))
    print("bill of dhosa = ",300*d)
elif op=="m":
    m=int(input("Enter quantity of maggie =>"))
    print("bill of maggie = ",100*m)
elif op=="s":
    s=int(input("Enter quantity of sandwhic =>"))
    print("bill of sandwhich = ",200*s)
elif op=="p":
    p=int(input("Enter quantity of panjabi dish => ",))
    print("bill of panjabi dish = ",300*p)
elif op=="g":
    
    g=int(input("Enter quantity of gujarati dish =>"))
    print("bill of gujarati dish = ",200*g)
else:
    print("Wrong option!!!")    




    
