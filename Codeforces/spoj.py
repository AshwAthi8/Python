t = int(input())
for i in range(t):
	c= 0
	n,m,a,d = list(map(int,input().split(" ")))
	for k in range(n,m+1,1):
		if(((k%a)!=0) and (k%(a+d)!=0) and (k%(a+2*d)!=0) and (k%(a+3*d)!=0) and (k%(a+4*d)!=0)):
			c=c+1

	print(c) 
