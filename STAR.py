print("STAR PATTERN TEXT PROGRAM")
while True:
    print(" ")
    word = input("Enter you text: ")
    for i in word:
        if i=='a' or i == 'A':
            for row in range(7):
                for col in range(5):
                    if ((col==0 or col==4) and row!=0) or ((row==0 or row==3)and (col>0 and col<4)):
                        print("*",end="")
                    else:
                        print(end=" ")
                print()
            print()

        elif i=='b' or i=='B':
            for row in range(7):
                for col in range(5):
                    if (col==0 or col==4) or ((row==0 or row==3 or row==6)and (col>0 and col<4)):
                        print("*",end="")
                    else:
                        print(end=" ")
                print()
            print()
        
        elif i=='c' or i=='C':
            for row in range(7):
                for col in range(5):
                    if (col==0)or ((row==0 or row==6) and (col>0)):
                        print("*",end="")
                    else:
                        print(end=" ")
                print()
            print()
        elif i=='d' or i=='D':
            for row in range(7):
                for col in range(5):
                    if (col==0) or (col==4 and (row!=0 and row!=6))or ((row==0 or row==6) and (col>0 and col<4)):
                        print("*",end="")
                    else:
                        print(end=" ")
                print()
            print()
        elif i=='e' or i=='E':
            for row in range(7):
                for col in range(5):
                    if col==0 or ((row==0 or row==3 or row==6)and (col>0)):
                        print("*",end="")
                    else:
                        print(end=" ")
                print()
            print()
        elif i=='f' or i=='F':   
            for row in range(7):
                for col in range(5):
                    if (col==0) or ((row==0 or row==3) and col>0):
                        print("*",end="")
                    else:
                        print(end=" ")
                print()
            print()
        elif i=='g' or i=='G':         
            for row in range(7):
                for col in range(6):
                    if col==0 or (col==4 and (row!=1 and row!=2))or ((row==0 or row==6)and (col>0 and col<4))or (row==3 and (col==3 or col==5)):
                        print("*",end="")
                    else:
                        print(end=" ")
                print()
            print()
        elif i=='h' or i=='H':        
            for row in range(7):
                for col in range(5):
                    if (col==0) or ((row==0 or row==3) and col>0):
                        print("*",end="")
                    else:
                        print(end=" ")
                print()
            print()
        elif i=='i' or i=='I':   
            for row in range(7):
                for col in range(5):
                    if col==2 or (row==0 and col!=2) or (row==6 and col<2):
                        print("*",end="")
                    else:
                        print(end=" ")
                print()
            print()
            
        elif i=='j' or i=='J':      
            for row in range(7):
                for col in range(5):
                    if col==2 or (row==0 and col!=2) or (row==6 and col<2):
                        print("*",end="")
                    else:
                        print(end=" ")
                print()
            print()
        elif i=='k' or i=='K':
            x=0
            j=4
            for row in range(7):
                for col in range(5):
                    if col==0 or (row==col+2 and col>1):
                        print("*",end="")
                    elif((row==x and col==j) and col>0):
                        print("*",end="")
                        x=x+1
                        j=j-1
                    else:
                        print(end=" ")
                print()
            print()
        elif i=='l' or i=='L': 
            for row in range(7):
                for col in range(5):
                    if col==0 or (row==6 and col>0):
                        print("*",end="")
                    else:
                        print(end=" ")
                print()
            print()
        elif i=='m' or i=='M':   
            for row in range(7):
                for col in range(7):
                    if col==0 or col==6 or ((row==col)and (col>0 and col<4))or (row==1 and col==5)or (row==2 and col==4):
                        print("*",end="")
                    else:
                        print(end=" ")
                print()
            print()
        elif i=='n' or i=='N':       
            for row in range(6):
                for col in range(6):
                    if col==0 or col==5 or (row==col and (col>0 and col<5)):
                        print("*",end="")
                    else:
                        print(end=" ")
                print()
            print()
        elif i=='o' or i=='O':
            for row in range(7):
                for col in range(5):
                    if ((col==0 or col==4) and (row!=0 and row!=6)) or ((row==0 or row==6) and (col>0 and col<4)):
                        print("*",end="")
                    else:
                        print(end=" ")
                print()
            print()
        elif i=='p' or i=='P': 
            for row in range(7):
                for col in range(5):
                    if col==0 or (col==4 and (row==1 or row==2)) or ((row==0 or row==3) and (col>0 and col<4)):
                        print("*",end="")
                    else:
                        print(end=" ")
                print()
            print()
        elif i=='q' or i=='Q':
            for row in range(8):
                for col in range(5):
                    if ((col==0 or col==4) and (row>0 and row<6)) or ((row==0 or row==6)and (col>0 and col<4))or (row==5 and col==1)or (row==7 and col==3):
                        print("*",end="")
                    else:
                        print(end=" ")
                print()
            print()
        elif i=='r' or i=='R':
            for row in range(7):
                for col in range(5):
                    if col==0 or (col==4 and (row!=0 and row!=3)) or ((row==0 or row==3) and (col>0 and col<4)):
                        print("*",end="")
                    else:
                        print(end=" ")
                print()
            print()
        elif i=='s' or i=='S':
            for row in range(7):
                for col in range(5):
                    if((row==0 or row==3 or row==6) and (col>0 and col<4)) or (col==0 and (row>0 and row<3)) or (col==4 and (row>3 and row<6)):
                        print("*",end="")
                    else:
                        print(end=" ")
                print()
            print()
        elif i=='t' or i=='T':
            for row in range(7):
                for col in range(5):
                    if col==2 or (row==0 and col!=2):
                        print("*",end="")
                    else:
                        print(end=" ")
                print()
            print()
        elif i=='u' or i=='U':
            for row in range(7):
                for col in range(5):
                    if col==0 or col ==4 and row!=6 or row==6 and col>0 and col<4 :
                       print("*",end="")
                    else:
                        print(end=" ")
                print()
            print()
        elif i=='v' or i=='V':
            x=0
            j=6
            for row in range(4):
                for col in range(7):
                    if row==col:
                        print("*",end="")
                    elif row==x and col==j:
                        print("*",end="")
                        x= x+1
                        j=j-1
                    else:
                        print(end=" ")
                print()
            print()
        elif i=='w' or i=='W':
            x= 0
            j = 3
            for row in range(4):
                for col in range(7):
                    if col==0 or col==6 or col==5 and row ==2 or col==4 and row==1:
                        print("*",end="")
                    elif row==x and col==j:
                        print("*",end="")
                        x=x+1
                        j=j-1
                    else:
                        print(end=" ")
                print()
            print()
        elif i=='x' or i=='X':
            x=0
            j=4
            for row in range(5):
                for col in range(5):
                    if row==x and col==j:
                        print("*",end="")
                        x= x+1
                        j=j-1
                    elif row==col:
                        print("*",end="")
                    else:
                        print(end=" ")
                print()
            print()
            
        elif i=='y' or i=='Y':
            for row in range(5):
                for col in range(5):
                    if col==2 and row>1 or  row==col and col<2 or row==0 and col==4 or row==1 and col==3:
                        print("*",end="")
                    else:
                        print(end=" ")
                print()
            print()
        elif i=='z' or i=='Z':
            x=1
            j=4
            for row in range(0,6):
                for col in range(0,6):
                    if row==0 or row==5:
                        print("*",end="")
                    elif row==x and col==j:
                        print("*",end="")
                        x= x+1
                        j=j-1
                    else:
                        print(end=" ")
                print()
