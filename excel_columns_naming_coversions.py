def return_excel_column_names(col):
	"""
		converting number to column name
	"""
	resulting_column_name = ""
	if col == 0:
		return "Column in excel should be started from 1."
	while(col>0):
		if col <= 26:
			resulting_column_name += chr(64+(col))
			break
		else:
			resulting_column_name += chr(64+(col % 26))
			col = col // 26
	return resulting_column_name[::-1]

col = 121453
print(return_excel_column_names(col))


def col2num(col):
	"""
		converting column name to column number
	"""
    num = 0
    for c in col:
        num = num * 26 + (ord(c.upper()) - ord('A')) + 1
    return num
print(col2num("FWQG"))
