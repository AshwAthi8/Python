n, t, k, d = list(map(int,input().split()))
rate = n*(k/t)
c = n - k
t1=0
t2=0
l=n
c=n
t1=0
while(c > 0):
	c = c - k
	t1=t1+t
while(l > 0):
	if(t2 < d):
		l = l - k
	else:
		l = l - 2*k
	t2=t2+t
	if(d<t):
		t2=t2 - (t - d)
if(t1==t2 and d!= t):
	t1=t1+1


if(t1 > t2):
	print("YES")
else:
	print("NO")