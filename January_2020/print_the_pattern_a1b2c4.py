def print_the_pattern(s):
	"""
		Input: aabcc
		Output: a2b1c2
	"""
	lis = [0] * 26
	result_string = ""
	if len(s) == 0:
		return "Please enter something to proceed."
	else:
		prev = s[0]
		count = 0
		for char in s:
			if prev != char:
				result_string += prev + str(lis[ord(prev)-97])
				lis[ord(prev)-97] = 0
			prev = char
			lis[ord(char)-97] += 1
			count += 1
			if count == len(s):
				result_string += prev + str(lis[ord(prev)-97])
		return result_string

string = "aabcddeeeeff"
print(print_the_pattern(string))   ##a2b1c1d2e4f2