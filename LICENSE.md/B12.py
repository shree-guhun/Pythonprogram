N=int(input("Enter Number:"))
temp=N
rev=0
while(N>0):
  dig=N%10
  rev=rev*10+dig
  N=N//10
if(temp==rev):
  print("The given number is a palindrome!")
else:
  print("The given number is not a palindrome!")
