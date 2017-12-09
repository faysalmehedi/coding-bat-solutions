#Given a string and a non-negative int n, 
#we'll say that the front of the string is the first 3 chars, 
#or whatever is there if the string is less than length 3. 
#Return n copies of the front;

def front_times(str, n):
	'''
	front_char = 3
	if len(str) < front_char:
		front_char = len(str)
	front = str[:front_char]
	return front * n'''

	if len(str) < 3:
		return str * 3
	return str[:3] * n


print(
front_times('Chocolate', 2),
front_times('Chocolate', 3),
front_times('bc', 3))