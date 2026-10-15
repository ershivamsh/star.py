x=int(input())
y=int(input())
n=int(input())
num=0
for i in range (x,y+1):
    if i%n!=0:
        num+=1
        print(i)
print(num)
print()