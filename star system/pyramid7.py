for i in range(10):
    for j in range(10):
        if i+j<5 or j-i>4 or i+j>13 or i-j>4:
            print("*", end="")
        else:
            print(" ", end="")
    print()