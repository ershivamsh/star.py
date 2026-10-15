for i in range(5):
    for j in range(9):
        if j-i>=4:
            print("*", end="")
        else:
            print(" ", end="")
    print()