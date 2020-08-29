def longestCommonSubsequence(text1,text2):
    print("hello")
    m,n = len(text1),len(text2)
    l = [[None]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if(i==0 or j == 0):
                l[i][j] = 0
            elif(text1[i-1] == text2[j-1]):
                l[i][j] = l[i-1][j-1] +1
            else:
                l[i][j] = max(l[i-1][j],l[i][j-1])
    return l[m][n]



print(longestCommonSubsequence("ashwathi","ash"))