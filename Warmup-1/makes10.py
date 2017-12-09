#Given 2 ints, a and b, 
#return True if one of them is 10 
#or if their sum is 10.

def makes10(a, b):
	#return (a == 10 or b == 10) or (a + b == 10)
	if a == 10 or b == 10 or a + b == 10:
		return True
	return False


print(
makes10(9, 10),
makes10(9, 9),
makes10(1, 9))