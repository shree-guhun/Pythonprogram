a=int(input("Enter the hour:"))
b=int(input("Enter the min:"))
c=int(input("Enter the hour1:"))
d=int(input("Enter the min1:"))
e=a*60+b
f=c*60+d
g1=e-f
print(g1//60,g1%60)
