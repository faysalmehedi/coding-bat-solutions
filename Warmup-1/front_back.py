#Given a string, return a new string where the first and last chars have been exchanged.


def front_back(str):
	if len(str) <= 1:
		return str
	return str[len(str)-1] + str[1:len(str)-1] + str[0]
	#alternative
	'''a = str[0]
	b = str[1:len(str)-1]
	c = str[len(str)-1:]
	return c + b + a'''


print(
front_back('code'),
front_back('a'),
front_back('ab'))