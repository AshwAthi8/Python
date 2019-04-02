#whitehat

file=bytearray(open("dump3", 'rb').read())
xord= bytearray(len(file)) 
for i in range(1,100):
	for j in range(len(file)):
		xord[j] = file[j]^i
	p="file"+str(i)
	f=open(p, 'wb')
	f.write(xord)
	f.close()
