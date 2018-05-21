x=int(input())
y=int(input())
b=str(x)
l=[]
for i in range(len(b)):
    l.append(b[i])
for i in range(y,len(b)):
    print(int(l[i]),end=' ')
 
