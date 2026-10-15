for i in range(5):
    for j in range(9):
        if i>=0 and(i>=j):
            print("*", end="")
        else:
            print(" ", end="")
    print()