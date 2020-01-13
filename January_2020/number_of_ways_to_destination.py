def finding_ways(m,n):
    """
        Calculate number of ways requires to traverse from top left cell to bottm right cell in matrix if only forward and downword movement is allowed.
        Input: Row 3
               Columns 3
        Output: 6
    """
    mat = [[0 for j in range(n)] for i in range(m)]

    #Initialize 1st element as 0 as there is no way to go to
    mat[0][0] = 0

    #Initilize 0th row to 1 as there is only one way to go to
    for i in range(1,m):
        mat[i][0] = 1

    #Initialize 0th column to 1 as there is only one way to go to    
    for j in range(1,n):
        mat[0][j] = 1

    #Calculate DP from (1,1)
    for i in range(1,m):
        for j in range(1,n):
            mat[i][j] = mat[i-1][j] + mat[i][j-1]
    return mat[m-1][n-1]

if __name__ == "__main__":    
    m=3
    n=3
    print(finding_ways(m,n))
