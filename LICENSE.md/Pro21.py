s1=0
l=[]
n=int(input())
for i in range(n):
	l.append(int(input()))
sub=n//2
for i in range(sub):
	s1+=l[i]
sub1=s1/sub
s1=0
for i in range(sub,n):
	s1+=l[i]
sub2=s1/(n-sub)
if sub1==sub2 :
	print('yes')
else :
	print('no')
