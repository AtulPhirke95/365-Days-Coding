"""
  Problem Statements: Give a N*N square matrix, return an array of its anti-diagonals. 
                      Look at the example for more details.
  Input: If the matrix is
          1 2 3
          4 5 6
          7 8 9
The output should Return the following :
          [ 
            [1],
            [2, 4],
            [3, 5, 7],
            [6, 8],
            [9]
          ]
"""

lis = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
N =5
lis = [[j+(N*(i-1)) for j in range(1,N+1)]for i in range(1,N+1)]
try:
	for i in range(0,N):
		i_=0
		j_=i
		while(i_<=i and j_>=0):
			print(lis[i_][j_])
			i_+=1
			j_-=1
except IndexError:
	pass

count= N - 1
try:
	for i in range(1,N+1):
		j = N - 1
		c_ = 0
		while(c_<count):
			print(lis[i][j])
			i+=1
			j-=1
			c_+=1
		count-=1
except:
	pass
