for i in range(9):
    for j in range(5):
        if i+j>8 or j>i:
            print(" ", end="")
        else:
            print("*", end="")
    print()