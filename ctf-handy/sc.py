from z3 import *
import random
​
def main():
​
    s = [ BitVec('s[%s]' % i, 8) for i in range(38) ]
    checkstring="qtqnhuyj{fjw{rwhswzppfnfrz|qndfktceyba"
    #l=list(checkstring)
    sol = Solver()
    s = toNumbers(s)
#    sol.add(s.count())
    #print(s)
    for i in range(len(s)):
        sol.add(And(s[i]>96,s[i]<124))

    sol.add(s[0] == ord('f'))
    sol.add(s[1] == ord('l'))
    sol.add(s[2] == ord('a'))
    sol.add(s[3] == ord('g'))
    sol.add(s[4] == ord('{'))
    sol.add(s[37] == ord('}'))
    sol.add(s.count('q') == 3)
    
    while(s.check() == sat):
        m = (sol.model())
        w = ''
        for i in range(63):
            w += chr(m[m[i]].as_long())
        print(w)
​
def toNumbers(s):
    res = [None]*len(s)
    res[0] = random.randint(97,123)
    for i in range(1,len(s)):
        if(s[i-1] % 2 == 0):
            res[i] = s[i] + res[i-1] - 97
        else:
            res[i] = s[i] - res[i-1] - 97
        res[i] = (res[i] - 97 + 29)%29 + 97
    return(res)
​
def swapArray(s):
    #print(s)
    for i in range(38):
        k=i-1
        if(s[k] <= s[i]):
            flip(s,i,i-1)
    return s
​
def flip(s,i,j):
    temp = s[i]
    s[i] = s[j]
    s[j] = temp
​
main()
​
'''
In [18]: def rev(s):
    ...:     res=[None]*38
    ...:     for x in range(97,123):
    ...:         res[0]=ord(x)
    ...:         for i in range(1,38):
    ...:
​
​
checkstring="qtqnhuyj{fjw{rwhswzppfnfrz|qndfktceyba"
'''