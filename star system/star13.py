for i in range (1,10):
    for j in range (1,6):
        if i==1 or i==5 or i==9 :
            if j==1 or j==5:
                print(" ",end="")
            else:
                print("*",end="")
        elif j==1 or j==5:
            print("*",end="")
        else:
            print(" ",end="")
    print()