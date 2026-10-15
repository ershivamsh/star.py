for i in range(5):
    for j in range(9):
        if i>0 and(i>=j+1) or j-i>=5:
            print(" ", end="")
        else:
            print("*", end="")
    print()