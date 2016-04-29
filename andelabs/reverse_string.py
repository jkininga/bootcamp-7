def reverse_string(string):
	reverse_string= ''
	if string is not "":
		for b in string:
			rev_string = b+rev_string
		if rev_string == string:
			return True
		return rev_string
	else:
		return None


# print reverse_string('caro')