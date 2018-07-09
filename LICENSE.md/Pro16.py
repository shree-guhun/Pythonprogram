n=int(input())
l=[]
a=0
for i in range(n):
    a=int(input())
    l.append(a)
l.sort()
candy=0
c=0
for i in range(n):
    candy=candy+l[i]
print(candy)
