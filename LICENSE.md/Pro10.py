	s=0
	l=[]
	n1=int(input())
	for i in range(n1):
		l.append(int(input()))
	for i in l:
		s+=(n1-i)
	print(s)
