t=input()

al=0
di=0

for j in t:
    x=ord(j)
    if 97<=x<=122:
        al+=1
    else:
        di+=1
print("alphabets:",al)
print("Digits:",di)
