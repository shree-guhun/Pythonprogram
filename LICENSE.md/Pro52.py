min=999
(r,l1)=([],[])
for i in range(4):
	for j in range(2):
		l1.append(int(input()))
	r.append(l1)
	for m in l1:
		if min>m:
			min=m
	l1=[]
f=1
for i in range(len(r)):
	dif=r[i][0]-r[i][1]
	if dif in(0,-min,min):
		continue
	else :
		f=0
		break
if f!=0:
	print('yes')
else :
	print('no')
