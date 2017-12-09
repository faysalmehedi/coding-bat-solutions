#Given a string, we'll say that the front is the first 3 chars of the string. 
#If the string length is less than 3, the front is whatever is there. 
#Return a new string which is 3 copies of the front.

def front3(str):
	if len(str) < 3:
		return str * 3
	return str[:3] * 3
	'''front_end = 3
    if len(str) < front_end:
        front_end = len(str)
    front = str[:front_end]
    return front * 3 # front + front + front'''


print(
front3('Java'),
front3('chocolate'),
front3('abc')
)
