
place = [[6,6,6,6,6,6,6,0],[4,6,6,6,2,6,6,6],[6,6,3,6,6,6,6,1],[6,6,6,6,6,6,6,6],[6,6,6,6,6,6,6,6],[6,6,6,6,6,6,6,6],[6,6,6,6,6,6,6,6],[6,6,6,6,6,2,1,0]]

#4rook
#3hourse
#2bishop
#1queen
#0king
#5pawn
#6empty

#place = [[4,3,2,1,0,2,3,4],[5,5,5,5,5,5,5,5],[6,6,6,6,6,6,6,6],[6,6,6,6,6,6,6,6],[6,6,6,6,6,6,6,6],[6,6,6,6,6,6,6,6],[5,5,5,5,5,5,5,5],[4,3,2,1,0,2,3,4]]
#nplace =[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1]]
k=1
c=0
while(k):
	flag = 0  
	t = 0
	'''
	print("==========",c,"==========")

	print("From")
	x1 = input()
	print("To")
	x2 = input()	
	a,b = 8-(ord(x1[0])-48),ord(x1[1])-65
	c,d = 8-(ord(x2[0])-48),ord(x2[1])-65
	if(nplace[a][b] == nplace[c][d]):
		print("Invalid")
		exit(0)
	else:
		temp = place[a][b]
		ntemp = nplace[a][b] 
		place[a][b] = place[c][d]
		nplace[a][b]= nplace[c][d]
		place[c][d] = temp
		nplace[c][d] = ntemp
	'''
	for i in range(8):
		for j in range(8):
			x,y = 8-i,j+9
			if(place[i][j] == 0):
				t = x+y
				flag = flag + t
			elif(place[i][j] == 1):
				t = x*y
				flag = flag + t
			elif(place[i][j] == 2):
				t = 2*(x+y)
				flag = flag + t
			elif(place[i][j] == 3):
				t = y%x
				flag = flag + t
			elif(place[i][j] == 4):
				t = 256-x-y
				flag = flag + t
			elif(place[i][j] == 5):
				t = x-y
				flag = flag + t
			elif(place[i][j] == 6):
				flag = flag	
			else:
				print("Nothg")

			

	if(hex(flag)==0x1d3):
		print(place)
		k=0	
	else:
		print("sorry",hex(flag))
		k=0

#print(a,b,c,d)
#print(place[a][b], place[c][d])
#print(16*(a*8+b))
