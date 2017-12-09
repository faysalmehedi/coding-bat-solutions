#Given two int values, return their sum. 
#Unless the two values are the same, 
#then return double their sum.


def sum_double(a, b):
	if a == b:
		return (a + b) * 2
	return a + b


print(
sum_double(1, 2),
sum_double(3, 2), 
sum_double(2, 2)) #3 5 8