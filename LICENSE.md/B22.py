a=[]
n1=int(input())
for i in range(1,n1+1):
    b=int(input())
    a.append(b)
a.sort()
print(a[n1-1])
