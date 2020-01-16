"""
    1)forming a palindrome from string
    2)finding maximum length palindrome from the string which is not contigeous
    Given a string, find the minimum number of characters to be inserted to convert it to palindrome.
    For Example:
    ab: Number of insertions required is 1. bab or aba
    aa: Number of insertions required is 0. aa
    abcd: Number of insertions required is 3. dcbabcd
"""
def find_palindrome(s1,s2):
    m = len(s1)

    mat = [[0 for j in range(m+1)] for i in range(m+1)]
    #print(mat)
    for i in range(0,m+1):
        mat[i][0] = 0
    for j in range(0,m+1):
        mat[0][j] = 0

    for i in range(1,m+1):
        for j in range(1,m+1):
            if s1[i-1] == s2[j-1]:
                mat[i][j] = 1 + mat[i-1][j-1]
            else:
                mat[i][j] = max(mat[i-1][j],mat[i][j-1])

    print(m - mat[m][m]) #3
    

s1 = "geeks"
s2 = s1[::-1]
find_palindrome(s1,s2)
