d=0
n=x=int(input("enter no:"))
while n!=0:
    n=n//10
    d=d+1
a=x//10**(d-1)
b=x%10
t=(x%10**(d-1))//10
print(b,t,a)
