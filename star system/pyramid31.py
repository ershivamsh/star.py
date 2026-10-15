for i in range(5):
    for j in range(9):
        if i<=j and (i+j)<9:
            print("*", end="")
        else:
            print(" ", end="")
    print()