lo=int(input())
up=int(input())
for num1 in range(lo,up):
  if num1>1:
    for i in range(2,num1):
      if(num1%i)==0:
        break
    else:
      print(num1)
