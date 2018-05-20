while True:
  print("Enter '0' for exit.")
  chr=input("Enter any character:")
  if chr=='0':
         break
  else:
    if((chr>='a' and chr<='z')or (chr>='A'and chr<='Z')):
      print(chr,"is an alphabet.\n")
    else:
      print(chr,"is not an alphabet.\n")
