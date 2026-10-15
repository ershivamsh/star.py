n=int(input())
s=0
b=0
x=0
while x!=-999:
    x=int(input())
    if x>n:
        b+=1
    else:
        s+=1
print(b)
print(s)