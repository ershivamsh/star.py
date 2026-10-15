x=input().lower()
al=0
di=0
sp=0
sc=0
for i in x:
    if i.isalpha():
        al+=1
    elif i.isdigit():
        di+=1
    elif i==" ":
        sp+=1
    else:
        sc+=1
print("alphabets:",al)
print("Digits:",di)
print("Spaces:",sp)
print("Sc:",sc)
