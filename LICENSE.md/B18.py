l=int(input())
u=int(input())
for N in range(l,u):
  sum=0
  temp=N
  while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
  if N==sum:
   print(N)
