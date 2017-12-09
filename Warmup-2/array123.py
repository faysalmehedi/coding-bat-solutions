#Given an array of ints, 
#return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

def array123(nums):
	for n in range(len(nums)-2):
		if nums[n] == 1 and nums[n+1]==2 and nums[n+2] == 3:
			return True
	return False



print(
array123([1, 1, 2, 3, 1]),
array123([1, 1, 2, 4, 1]),
array123([1, 1, 2, 1, 2, 3]))