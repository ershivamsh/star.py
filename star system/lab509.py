n=int(input())
d=int(input())
t=0
while n!=0:
    x=n%10
    n=n//10
    if x==d:
        t+=1
print(t)