def _lcm(l,m):
	#if(len(l)==2):
	if(l>m):
		num1 = l		
		num2 = m
	else:
		num1 = m
		num2 = l	
	rem = num1%num2
	while(rem != 0):
		num1 = num2
		num2 = rem
		rem = num1%rem
	gc = num2		
	lc = int(int(l*m/int(gc)))
	return lc



t = int(input())

for i in range(t):
	c= 0
	n,m,a,d = list(map(int,input().split(" ")))
	c = (int(m/a) + int(m/(a+d)) + int(m/(a+2*d) + int(m/(a+3*d)  + int(m/(a+4*d) - int((n-1)/a -int((n-1)/(a+d)) - int((n-1)/(a+2*d) - int((n-1)/(a+3*d)  - int((n-1)/(a+4*d))) 
		- (m/lcm(a,a+d) + m/lcm(a,a+2*d) + m/lcm(a,a+3*d) + lcm(a,a+4*d) + m/lcm(a+d,a+2*d) + m/lcm(a+d,a+3*d) + m/lcm(a+d,a+4*d) + 
		+ () 
		- ()
	''' 	 	
	for k in range(n,m+1,1):
		if(((k%a)!=0) and (k%(a+d)!=0) and (k%(a+2*d)!=0) and (k%(a+3*d)!=0) and (k%(a+4*d)!=0)):
			c=c+1
 	'''
	print(c) 