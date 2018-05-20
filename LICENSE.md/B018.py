l=int(input())
u=int(input())
for N1 in range(l,u):
  sum=0
  temp=N1
  while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
  if N1==sum:
   print(N1)
