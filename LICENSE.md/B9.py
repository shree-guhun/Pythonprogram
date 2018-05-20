N=int(input("N:"))
K=int(input("K:"))
M=[]
s=0
for i in range(0,N):
a=input()
M.append(a)
for i in range(0,K):
s=s+int(M[i])
print(s)
