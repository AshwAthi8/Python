s = list(input().split(" "))
s.append(0)
k = len(s)
i=0
c=1
while(i<k-1):
    if(s[i]==s[i+1]):
        c=c+1
    else:
        print(s[i]+str(c),end='')
        c=1
    i=i+1

'''
a a b
['a', 'a', 'b', 0]
a2b1
'''
