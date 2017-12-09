#Given an int n, return True if it is within 10 of 100 or 200. 
#Note: abs(num) computes the absolute value of a number.


def near_hundred(n):
	return abs(100 - n) <= 10 or abs(200 - n) <=10
	
	#return 90<=n<=110 or 190<=n<=210


print(
near_hundred(93),
near_hundred(90),
near_hundred(89))