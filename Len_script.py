#challenge100.exe - INCTF 

for i in range(200):
	p=i<<3
	a=#30
	s=a*2 				#0x168
	a=hex(s*1272582903)
	p1=int(a[:4],16)>>3 		#0x6a>>3 = 0xd
	s1=s>>31 			#0
	l=p1-s1 			#0xd
	p2=2*l + p1 			#0x27
	p3=p2*8 			#0x138
	p4=p2+p3 			#0x157
	p5=s-p4 			#9
	
	if(p5==0 and l==20):
		print(i)

#30
