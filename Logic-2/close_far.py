#Given three ints, a b c, return True if one of b or c is 
#"close" (differing from a by at most 1), while the other is 
#"far", differing from both other values by 2 or more. 
#Note: abs(num) computes the absolute value of a number.

def close_far(a, b, c):
	if abs(a-b) >= 1:
		if abs(a-c) >= 2 and abs(b-c) >= 2:
			return True
	if abs(a-c) >= 1:
		if abs(a-b) >= 2 and abs(b-c) >= 2:
			return True
	return False

'''
def close_far(a, b, c):
	return (close(a,b) and far(a,b,c)) or (close(a,c) and far(a,c,b))

def close(x,y):
	return abs(x-y) <= 1
def far(x,y,z):
	return abs(x-z) >= 2 and abs(y-z) >= 2
'''



print(
close_far(1, 2, 10),
close_far(1, 2, 3),
close_far(4, 1, 3))
