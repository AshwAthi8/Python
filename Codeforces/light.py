import math
c= 1
while(c):
	p = int(input())
	if(p != 0 ):
		l = 0
		'''
		for k in range(1,int(math.sqrt(p))+1):
			if((p%k) == 0 ):
				l = l+1
		if(l%2 == 0 ):
			print("yes")
		else:
			print("no")
		'''
		if(((math.sqrt(p))-int(math.sqrt(p)))==0):
			print("yes")
		else:
			print("no")
	else:
		c = 0
