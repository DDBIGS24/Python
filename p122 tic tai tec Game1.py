game=['_','_','_','_','_','_','_','_','_']
t=1
while t<10:
   
    if t%2==0:
        pos1=int(input("Enter Dishant position =>"))
        if game[pos1 - 1] =="_":
                game[pos1-1] = 'X'
        else:
            print("Error !!!")
            t-=1      
    else:
        pos2=int(input("Enter Chinmay position =>"))
        game[pos2-1] = '0'
        if game[pos2 - 1] == "_":
                game[pos2-1] = "0"
        else:        
            print("Error !!!")
            t-=1

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
    elif game[3] == game[4] == game[5] =="X":
        print("Dishant is winner")
        t=15
    elif game[3] == game[4] == game[5] =="0":
        print("Chinmay is winner")
        t=15
    elif game[6] == game[7] == game[8] =="X":
        print("Dishant is winner")  
        t=15 
    elif game[6] == game[7] == game[8] =="0":
        print("Chinmay is winner")  
        t=15
    elif game[0] == game[3] == game[6] =="X":
        print("Dishant is winner") 
        t=15   
    elif game[0] == game[3] == game[6] =="0":
        print("Chinmay is winner")  
        t=15
    elif game[1] == game[4] == game[7] =="X":
        print("Dishant is winner")  
        t=15
    elif game[1] == game[4] == game[7] =="0":
        print("Chinmay is winner")  
        t=15
    elif game[2] == game[5] == game[8] =="X":
        print("Dishant is winner")  
        t=15 
    elif game[2] == game[5] == game[8] =="0":
        print("Chinmay is winner")  
        t=15     
    elif game[2] == game[4] == game[6] =="X":
        print("Dishant is winner")  
        t=15
    elif game[2] == game[4] == game[6] =="0":
        print("Chinmay is winner") 
        t=15                             
    elif game[0] == game[4] == game[8] =="X":
        print("Dishant is winner")  
        t=15
    elif game[0] == game[4] == game[8] =="0":
        print("Chinmay is winner")  
        t=15
    t+=1
# print("t = ",t)
if t == 10:
        print("Tie!!!")