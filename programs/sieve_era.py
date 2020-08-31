def countPrimes(n):
        p=2
        if(n <= 2):
            return 0
        pr = [True for i in range((n))]
        while(p*p<=n):
            if(pr[p]==True):
                for i in range(p*p,n,p):
                    pr[i] = False
            p=p+1
        c=0
        for i in range(2,n):
            if(pr[i]):
                c=c+1
             
        return c
            
print(countPrimes(int(input())))