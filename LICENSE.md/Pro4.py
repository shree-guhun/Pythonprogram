x=input()
y=input()
c1=0
for i in range(len(x)):
    d1=ord(x[i])-ord(y[i])
    print(d1)
    c1=c1+d1
print(c1)
