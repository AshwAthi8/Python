
from z3 import *
s=Solver()
n = [
BitVec("n[0]", 8),
BitVec("n[1]", 8),
BitVec("n[2]", 8),
BitVec("n[3]", 8),
BitVec("n[4]", 8),
BitVec("n[5]", 8),
BitVec("n[6]", 8)]

m = [
BitVec("m[0]", 8),
BitVec("m[1]", 8),
BitVec("m[2]", 8),
BitVec("m[3]", 8),
BitVec("m[4]", 8),
BitVec("m[5]", 8),
BitVec("m[6]", 8),
BitVec("m[7]", 8),
BitVec("m[8]", 8),
BitVec("m[9]", 8),
BitVec("m[10]", 8),
BitVec("m[11]", 8),
BitVec("m[12]", 8),
BitVec("m[13]", 8),
BitVec("m[14]", 8),
BitVec("m[15]", 8),
BitVec("m[16]", 8),
BitVec("m[17]", 8),
BitVec("m[18]", 8),
BitVec("m[19]", 8),
BitVec("m[20]", 8),
BitVec("m[21]", 8),
BitVec("m[22]", 8),
BitVec("m[23]", 8),
BitVec("m[24]", 8),
BitVec("m[25]", 8),
BitVec("m[26]", 8),
BitVec("m[27]", 8),
BitVec("m[28]", 8),
BitVec("m[29]", 8),
BitVec("m[30]", 8),
BitVec("m[31]", 8),
BitVec("m[32]", 8),
BitVec("m[33]", 8),
BitVec("m[34]", 8),
BitVec("m[35]", 8),
BitVec("m[36]", 8),
BitVec("m[37]", 8),
BitVec("m[38]", 8),
BitVec("m[39]", 8),
BitVec("m[40]", 8),
BitVec("m[41]", 8),
BitVec("m[42]", 8),
BitVec("m[43]", 8),
BitVec("m[44]", 8),
BitVec("m[45]", 8),
BitVec("m[46]", 8),
BitVec("m[47]", 8),
BitVec("m[48]", 8),
BitVec("m[49]", 8),
BitVec("m[50]", 8),
BitVec("m[51]", 8),
BitVec("m[52]", 8),
BitVec("m[53]", 8),
BitVec("m[54]", 8),
BitVec("m[55]", 8),
BitVec("m[56]", 8),
BitVec("m[57]", 8),
BitVec("m[58]", 8),
BitVec("m[59]", 8),
BitVec("m[60]", 8),
BitVec("m[61]", 8),
BitVec("m[62]", 8),]




a = 'abcdefghijklmnopqrstuvwxyz'
p = ' !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'




for i in range(len(n)):
    s.add(z3.And(n[i] >= 61  , n[i] <= 122))

for i in range(len(m)):
	s.add(z3.And(m[i] >= 32  , m[i] <= 47))
	s.add(z3.And(m[i] >= 58  , m[i] <= 64))
	s.add(z3.And(m[i] >= 91  , m[i] <= 126))



s.add(m[0]^n[0]^n[0]^n[0] == 1)
s.add(m[1]^n[0]^n[1]^n[0] == 18)
s.add(m[2]^n[0]^n[2]^n[0] == 21)
s.add(m[3]^n[1]^n[0]^n[0] == 18)
s.add(m[4]^n[1]^n[1]^n[0] == 73)
s.add(m[5]^n[1]^n[2]^n[0] == 20)
s.add(m[6]^n[2]^n[0]^n[0] == 65)
s.add(m[7]^n[2]^n[1]^n[0] == 8)
s.add(m[8]^n[2]^n[2]^n[0] == 8)
s.add(m[9]^n[3]^n[0]^n[0] == 4)
s.add(m[10]^n[3]^n[1]^n[0] == 24)
s.add(m[11]^n[3]^n[2]^n[0] == 24)
s.add(m[12]^n[4]^n[0]^n[0] == 9)
s.add(m[13]^n[4]^n[1]^n[0] == 18)
s.add(m[14]^n[4]^n[2]^n[0] == 29)
s.add(m[15]^n[5]^n[0]^n[0] == 21)
s.add(m[16]^n[5]^n[1]^n[0] == 3)
s.add(m[17]^n[5]^n[2]^n[0] == 21)
s.add(m[18]^n[6]^n[0]^n[0] == 14)
s.add(m[19]^n[6]^n[1]^n[0] == 6)
s.add(m[20]^n[6]^n[2]^n[0] == 18)
s.add(m[21]^n[0]^n[0]^n[1] == 83)
s.add(m[22]^n[0]^n[1]^n[1] == 2)
s.add(m[23]^n[0]^n[2]^n[1] == 26)
s.add(m[24]^n[1]^n[0]^n[1] == 86)
s.add(m[25]^n[1]^n[1]^n[1] == 83)
s.add(m[26]^n[1]^n[2]^n[1] == 5)
s.add(m[27]^n[2]^n[0]^n[1] == 20)
s.add(m[28]^n[2]^n[1]^n[1] == 27)
s.add(m[29]^n[2]^n[2]^n[1] == 28)
s.add(m[30]^n[3]^n[0]^n[1] == 85)
s.add(m[31]^n[3]^n[1]^n[1] == 67)
s.add(m[32]^n[3]^n[2]^n[1] == 5)
s.add(m[33]^n[4]^n[0]^n[1] == 17)
s.add(m[34]^n[4]^n[1]^n[1] == 2)
s.add(m[35]^n[4]^n[2]^n[1] == 7)
s.add(m[36]^n[5]^n[0]^n[1] == 12)
s.add(m[37]^n[5]^n[1]^n[1] == 11)
s.add(m[38]^n[5]^n[2]^n[1] == 17)
s.add(m[39]^n[6]^n[0]^n[1] == 0)
s.add(m[40]^n[6]^n[1]^n[1] == 2)
s.add(m[41]^n[6]^n[2]^n[1] == 20)
s.add(m[42]^n[0]^n[0]^n[2] == 12)
s.add(m[43]^n[0]^n[1]^n[2] == 26)
s.add(m[44]^n[0]^n[2]^n[2] == 26)
s.add(m[45]^n[1]^n[0]^n[2] == 30)
s.add(m[46]^n[1]^n[1]^n[2] == 15)
s.add(m[47]^n[1]^n[2]^n[2] == 44)
s.add(m[48]^n[2]^n[0]^n[2] == 15)
s.add(m[49]^n[2]^n[1]^n[2] == 31)
s.add(m[50]^n[2]^n[2]^n[2] == 0)
s.add(m[51]^n[3]^n[0]^n[2] == 12)
s.add(m[52]^n[3]^n[1]^n[2] == 46)
s.add(m[53]^n[3]^n[2]^n[2] == 8)
s.add(m[54]^n[4]^n[0]^n[2] == 28)
s.add(m[55]^n[4]^n[1]^n[2] == 23)
s.add(m[56]^n[4]^n[2]^n[2] == 0)
s.add(m[57]^n[5]^n[0]^n[2] == 11)
s.add(m[58]^n[5]^n[1]^n[2] == 3)
s.add(m[59]^n[5]^n[2]^n[2] == 25)
s.add(m[60]^n[6]^n[0]^n[2] == 14)
s.add(m[61]^n[6]^n[1]^n[2] == 0)
s.add(m[62]^n[6]^n[2]^n[2] == 65)

m[1]==m[3]
m[5] == m[27] 
m[21] == m[25]
m[23] == m[43]

print("-------------starting-------------------")
while(s.check() != sat):

    print("-----checking----")
    m = (s.model())
    n = (s.model())
    w = ''
    v = ''
    for i in range(63):
        w += chr(m[m[i]].as_long())
    print(w)
    for i in range(7):
        v += chr(n[n[i]].as_long())

    print("----- m is -----  ",w)
    print("----- n is -----  ",v)
print("--------------ending------------------")

