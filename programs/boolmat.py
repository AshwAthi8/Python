def setZeroes(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        rmat = [0]*r
        cmat = [0]*c
        
        for i in range(r):
            for j in range(c):
                if(matrix[i][j] == 0):
                    rmat[i] = 1 
                    cmat[j] = 1
        for i in range(r):
            for j in range(c):
                if(rmat[i] == 1 or cmat[j] ==1):
                    matrix[i][j] = 0


