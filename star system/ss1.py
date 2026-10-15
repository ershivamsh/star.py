x1=int(input("x1"))
x2=int(input("x2"))
y1=int(input("y1"))
y2=int(input("y2"))
r=int(input("radius"))
d=((x2-x1)**2+(y2-y1)**2)**(1/2)
if d>r:
    print("outside")
elif (d==r):
     print("on the circle")
else:
    print("inside the circle")