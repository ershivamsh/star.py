d=0
n=x=int(input("enter no:"))
while n!=0:
    n=n//10
    d=d+1
print(x//10**(d-1) + d%10)
