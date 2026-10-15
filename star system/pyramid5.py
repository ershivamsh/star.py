for i in range(9):
    for j in range(5):
        if i+j<4 or i-j>4:
            print(" ", end="")
        else:
            print("*", end="")
    print()