#Given a string, return the count of the number of times that a substring length 2 
#appears in the string and also as the last 2 chars of the string, 
#so "hixxxhi" yields 1 (we won't count the end substring).

def last2(str):
	#screen out for too short length
	if len(str) < 2:
		return 0
	#last 2 char must be str[-2:]
	last2 = str[len(str)-2:]
	count = 0
	#check the each substring length 2 starting at i
	for i in range(len(str)-2):
		sub = str[i:i+2]
		if sub == last2:
			count += 1
	return count



print(
last2('hixxhi'),
last2('xaxxaxaxx'),
last2('axxxaaxx'))