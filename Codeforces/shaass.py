n = int(input())
a = list(map(int,input().split()))
k = int(input())
for i in range(k):
	p,q = list(map(int,input().split()))
	if(p==1 and (len(a)>1)):
		a[p] = a[p-1] - q + a[p]
		a[p-1] = 0

	elif(p==1 and (len(a) == 1)):
		a[p-1] = 0
	elif( p == len(a)):
		a[p-2] = a[p-2] + q - 1
		a[p-1] = 0
	else:
		a[p] = a[p-1] - q + a[p]
		a[p-2] = a[p-2] + q - 1
		a[p-1] = 0

for j in range(n):
	print(a[j])

