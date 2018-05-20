y=int(input("Enter the year:"))
if(y%4==0 and y!=100 or y%400==0):
  print(y,"is leap year")
else:
  print(y,"is not a leap year")
