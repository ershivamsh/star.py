x=input().lower()
vo=0
co=0
for i in x:
    if i in "aeiou":
        vo+=1
    else:
        co+=1
print("vovels:",vo)
print("consonents:",co)