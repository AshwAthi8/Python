s = input().replace(" ", "")

p = len(set(s))
if(p == 2):
	print(0)
elif(p == 3):
	print(1)
else:
	print(p-3)
	