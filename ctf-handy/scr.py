
from pwn import * 
import datetime
import pytz 
r = remote("privbd.pwn2.win",4321)
#s = r.recvuntil("Welcome to the Token Generator")
#print(s)


def val(a):
	ar = [34, 60, 62, 33, 64, 35, 36, 37, 94, 38, 42, 45, 47, 51, 52, 54, 56, 57, 63, 92, 96, 124, 59, 123, 125]
	for i in (a):
		if ord(i) in ar:
			return 1
	return 0


def gen_token(ser,seed,p5):
	p6 = []
	p7 = 0
	p8 = []
	p4 = ser ^ 2

	for i in (seed):
		if (ord(i) % 2) != 0:
			p6.append(ord(i))
	for i in range(0,6):
		for j in range(0,len(p6)):
			p8.append(p6[j])

	#print(p8, len(p8))
	for k in range(3,60):
		p7 = p7 + p8[k]

	p8 = p8[1] * p8[33] * p8[33] * p8[7] + p8[len(p8)-1] + p8[len(p8)-1-32] + p8[len(p8)-1-32]  + p8[len(p8)-1-6] + p7
	#k = 
	print( (abs(p4 - (p5+p8))))
	return (abs(p4 - (p5+p8)))

def main_function():
	serial = "7221"
	seed = "eicuSh7eehaesheef4OoCeoghai4KaisauXughuu"

	if((val(serial) ==0) and(len(str(serial)) == 4)):
		timeZ = pytz.timezone("Brazil/East") 
		current = datetime.datetime.now(timeZ) 
		#print(current)
		ht = current.hour
		mt = current.minute
		day = current.day
		final_date = (ht * mt) + (day + 1) * (-1)
		return str((gen_token(int(serial,10),seed,final_date)))

r.sendline((main_function()))
