N1=int(input())
sum=0
temp=N1
if N1<=100000:
  while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
  if N1==sum:
   print("yes")
  else:
    print("No")
else:
  print("please enter correct input")
