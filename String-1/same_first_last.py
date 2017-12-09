#Given an array of ints, 
#return True if the array is length 1 or more, 
#and the first element and the last element are equal.

def same_first_last(nums):
	'''if len(nums) >= 1:
		if nums[0] == nums[-1]:
			return True
	return False'''

	return len(nums) >= 1 and nums[0] == nums[-1]

print(
same_first_last([1, 2, 3]),
same_first_last([1, 2, 3, 1]),
same_first_last([1, 2, 1]))