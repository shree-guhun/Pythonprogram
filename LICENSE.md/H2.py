def f1(l):
	l.sort(reverse=True)
	s1=''
	c=0
	new=''
	for i in l:
		s1+=str(i)
		c+=1
	print(s1)
	c=0
	for i in range(len(s1)-1,-1,-1):
		if c==3:
			c=0
			new+=','
		new+=s1[i]
		c=c+1
	print(new[::-1])
def main():
	try:
		n=int(input())
		l=[]
		for i in range(n):
			l.append(int(input()))
		f1(l)
	except:
		print('invalid')
main()
