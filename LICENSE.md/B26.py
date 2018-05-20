n1=int(input("enter n"))
a=0
b=a
l=[]
for i in range(0,n1):
    a=int(input())
    l.append(a)
    l.sort()
    if i==2:
        b=l[i]
print(b)
