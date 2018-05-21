def f(s,n,m):
	su1=0
	while(True):
		su1+=n+m
		if s==su1:
			return 'yes'
		if su1>s:
			break
	return 'no'
def main():
	n=int(input())
	a=int(input())
	b=int(input())
	print(f(n//2,a,b))
  
try:
  main()
except:
  print('invalid')
