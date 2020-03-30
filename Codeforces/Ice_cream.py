p,q = list(map(int,input().split()))
c = 0
t = 0
for i in range(p):
	a,b = list((input().split(" ")))
	x = int(b)
	if(a=='+'):
		#print("----Increatement----",x[0])
		q = x + q
	elif(a == '-'):
		if(q>=x):
			q=q-x
		else:
			c=c+1
		#	print("------count---",c)

print(q,c)