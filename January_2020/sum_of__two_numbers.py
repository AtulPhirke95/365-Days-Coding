def return_me_the_indexes(n,arr):
	"""
		Input: n = 7
		       arr = [2,3,7,4,12,35]
		Output: (1, 3) -> 3 + 4 = 7 
	"""
	temp_lis = []
	flag = False
	for i in range(len(arr)):
		if n - arr[i] in temp_lis:
			flag = True
			return arr.index(n - arr[i]), i
		else:
			temp_lis.append(arr[i])
	if flag == False:
		return "Not found"

n = 7
arr = [2,3,7,4,12,35]
print(return_me_the_indexes(n,arr))
