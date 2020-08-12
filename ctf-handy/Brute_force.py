import itertools

letters="1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
C=0
for c in itertools.permutations(letters,3):
	flag=(''.join(c))+"X"
	flag=flag[::-1]
	l=88
	for a in range(len(flag)):
		l=l^(ord(flag[a]))
									
	if(l==88):
		C=C+1
		print(flag) 
	else: 
		continue 
print(C)
