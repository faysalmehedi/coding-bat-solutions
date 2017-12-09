#Given an array of ints, return True if one of the first 4 elements in the array is a 9. 
#The array length may be less than 4.

def array_front9(nums):
	'''end = lens(nums)
	if len(nums) > 4:
		end = 4'''
	end = 4
	if len(nums) < 4:
		end = lens(nums)
	for n in range(end):
		if nums[n] == 9:
			return True
	return False



print(
array_front9([1, 2, 9, 3, 4]),
array_front9([1, 2, 3, 4, 9]),
array_front9([1, 2, 3, 4, 5]))