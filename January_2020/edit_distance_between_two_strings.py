def edit_distance(s1,s2):
	"""
		Edit distance means number of operations requires to convert one to another.
		Operations available are: Insert, Replace, Delete
		Input: S1 = saturday
			   S2 = sunday
		Output: 3	
	"""
	length_of_s1 = len(s1)
	length_of_s2 = len(s2)
	m = length_of_s1 +1
	n = length_of_s2 + 1
	edit_mat = [[0] * n for i in range(m)]

	for i in range(1,length_of_s1+1):
		edit_mat[i][0] = i
	for j in range(1,length_of_s2+1):
		edit_mat[0][j] = j
	
	for i in range(1,length_of_s1 + 1):
		for j in range(1,length_of_s2 + 1):
			if s1[i-1] == s2[j-1]:
				edit_mat[i][j] = edit_mat[i-1][j-1]
			else:
				edit_mat[i][j] = 1 + min(edit_mat[i-1][j],edit_mat[i][j-1],edit_mat[i-1][j-1])

	return edit_mat[length_of_s1][length_of_s2]
	

s1 = "mat"
s2 = "cat"
print(edit_distance(s1,s2))