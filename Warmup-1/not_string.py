#Given a string, return a new string where "not " has been added to the front. 
#However, if the string already begins with "not", return the string unchanged.

def not_string(str):
	'''if len(str) < 3 or str[0:3] != "not":
		return "not " + str
	else:
		return str'''

	'''if str[0:3] == 'not':
		return str
	return 'not ' + str'''

	if str.startswith('not'):
		return str
	return 'not ' + str


print(not_string('candy'),
not_string('x'),
not_string('not bad'))