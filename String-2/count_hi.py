#Return the number of times that the string "hi" appears anywhere in the given string.

def count_hi(str):
	count = 0
	for i in range (len(str)):
		if str[i:i+2] == 'hi':
			count += 1
	return count

print(
count_hi('abc hi ho'),
count_hi('ABChi hi'),
count_hi('hihi'))
