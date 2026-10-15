for i in range(5):
    for j in range(9):
        if i<=3 and(i+j <=3) or i+j==10 or i+j==11 or i+j==12 or i+j==9:
            print(" ", end="")
        else:
            print("*", end="")
    print()