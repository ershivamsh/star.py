for i in range(5):
    for j in range(9):
        if i==4 and j<5 or j==0 or j==i:
            print("*", end="")
        else:
            print(" ", end="")
    print()