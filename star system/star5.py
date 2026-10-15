for i in range(5):
    for j in range(9):
        if i==0 and j>3 or i+j==4 or i+j==9 or i==4 and j<=4:
            print("*", end="")
        else:
            print(" ", end="")
    print()