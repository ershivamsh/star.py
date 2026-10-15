t=int(input("Enter The Number:"))
a=(t//10000)
x=(t//1000)
b=(x%10)
y=(t//100)
c=(y%10)
z=(t%100)
d=(z//10)
e=(z%10)
if(a>b and a>c and a>d and a>e):
    print("a ")
elif(b>a and b>c and b>d and b>e):
    print("b ")
elif(c>a and c>b and c>d and c>e):
    print("c ")
elif(d>a and d>b and d>c and d>e):
    print("c ")
else:
    print("e ")
if(a>=b or a>=c or a>=d or a>=e):
    print("first")
elif(b>=c or b>=d or b>=e):
    print("second")
elif(c>=d or c>=e):
    print("third")
else:
    print("fourth")