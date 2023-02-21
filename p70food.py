d1=0
p1=0
g1=0
m1=0
f1=0
while True:
    print("press d for dhosa(100)")
    print("press p for panjabidish(250)")
    print("press g for gujaratidish(250)")
    print("press m for meggie(150)")
    print("press f for franki(100)")
    print("press e for exit")
    op=input("Enter option =>")

    if op=="d":
        d=int(input("Enter quanitiy of dhosa =>"))
        d1=100*d
        print("bill of dhosa = ",d1)
    elif op=="p":
        p=int(input("Enter quantity of panjabidish =>"))
        p1=250*p
        print("bill of panjabidish = ",p1)
    elif op=="g":
        g=int(input("Enter quantity of gujaratudish =>"))
        g1=250*g
        print("bill of gujaratidish = ",g1)
    elif op=="m":
        m=int(input("Enter quantity of maggie =>"))
        m1=150*m
        print("bill of maggie = ",m1)
    elif op=="f":
        f=int(input("Enter quantity of franki =>"))
        f1=100*f
        print("bill of franki = ",f1)
    elif op=="e":
        print("total = ",d1+p1+g1+m1+f1)
    else:
        print("Wrong Option!!!")

            