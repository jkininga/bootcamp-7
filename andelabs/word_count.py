def words(word):
	for c in word:
			string_list = word.split()

	string_dict = {}

	for word in string_list:
		if word in string_dict:
			string_dict[word] = string_dict[word] + 1
		else:
			string_dict[word] = 1
	return string_dict

string = "olly olly in come come free"
print words(string)
print words('go Go GO')