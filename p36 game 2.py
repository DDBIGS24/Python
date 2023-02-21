game=['_','_','_','_','_','_','_','_','_']
t=15
while t<10:

    if t%2==0:
        pos1=int(input("Enter Dishant position =>"))
        game[pos1-1] = 'X'
    else:
        pos2=int(input("Enter Chinmay position =>"))
        game[pos2-1] = '0'


    print("After turn ",t)
    print(game[0]," | ",game[1]," | ",game[2])
    print(game[3]," | ",game[4]," | ",game[5])
    print(game[6]," | ",game[7]," | ",game[8])
    if game[0] == game[1] == game[2] =="X":
        print("Dishant is winner")
        t=15
    elif game[0] == game[1] == game[2] =="0":
        print("Chinmay is winner")
        t=15
    elif game[3] == [4] == [5] =="X":
        print("Dishant is winner")
        t=15
    elif game[3] == [4] == [5] =="0":
        print("Chinmay is winner")
        t=15
    elif game[6] == [7] == [8] =="X":
        print("Dishant is winner")  
        t=15 
    elif game[6] == [7] == [8] =="0":
        print("Chinmay is winner")  
        t=15
    elif game[0] == [3] == [6] =="X":
        print("Dishant is winner") 
        t=15   
    elif game[0] == [3] == [6] =="0":
        print("Chinmay is winner")  
        t=15
    elif game[1] == [4] == [7] =="X":
        print("Dishant is winner")  
        t=15
    elif game[1] == [4] == [7] =="0":
        print("Chinmay is winner")  
        t=15
    elif game[2] == [5] == [8] =="X":
        print("Dishant is winner")  
        t=15 
    elif game[2] == [5] == [8] =="0":
        print("Chinmay is winner")  
        t=15     
    elif game[2] == [4] == [6] =="X":
        print("Dishant is winner")  
        t=15
    elif game[2] == [4] == [6] =="0":
        print("Chinmay is winner")  
        t=15                             
    elif game[0] == [4] == [8] =="X":
        print("Dishant is winner")  
        t=15
    elif game[0] == [4] == [8] =="0":
        print("Chinmay is winner")  
        t=15
    else:
        print("Wron position!!!")
    t+=1