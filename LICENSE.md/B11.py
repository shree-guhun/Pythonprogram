def power(b,E)
  if(E==1):
    return(b)
  if(E!=1):
    return(b*power(b,E-1))
b=int(input("Enter base:"))
E=int(input("Enter exponential value:"))
print("Result:",power(b,E))
