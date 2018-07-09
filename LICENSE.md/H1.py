def fre(li):
	li.sort()
	rep=[]
	n1=len(li)
	for i in range(1,n1):
			if li[i]==li[i-1] :
				if li[i] in rep :
					continue
				rep.append(li[i])
	print(rep)

def main():
	try:
		li=[]
		n1=int(input())
		for i in range(n1):
			li.append(int(input()))
		fre(li)
	except:
		print('invalid')

main()
