n=int(input())
m=list(map(int,input().split()))
l = (min(m.count(1),m.count(2),m.count(3)))
print(l)
d=0
j=n
for i in range(l):
        a = 0
        b = 0
        c = 0
        p=1
        while(p):
         
            if(m[d%j]==1):
                a= d%j +1
                m[d%j] = 0
                d=d+1
            if(m[d%j]==2):
                b= d%j +1 
                m[d%j] = 0
                d=d+1
            if(m[d%j]==3):
                c= d%j +1 
                m[d%j] = 0
                d=d+1
            if( a!=0 and b!=0 and c!=0):
                print(a,b,c)
                p = 0
                break 
                
