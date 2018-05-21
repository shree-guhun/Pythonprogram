from string import ascii_lowercase as asc_lower
def check(s1):
    return set(asc_lower) - set(s1.lower()) == set([])
str1=input("Enter string:")
if(check(str1)==True):
      print("The string is a pangram")
else:
      print("The string isn't a pangram")
