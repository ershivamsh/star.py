for i in range (9):
    for j in range (9):
        if i==j or i+j==8:
            print("+",end="")
        else:
            print(" ",end="")
    print()