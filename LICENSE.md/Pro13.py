m=int(input())
n=int(input())
l=[]
l1=[]
for i in range(m):
    a1=int(input())
    l.append(a1)
for j in range(n):
    u=int(input())
    v=int(input())
    for i in range(u,v):
        l1.append(l)
    print(min(l))
