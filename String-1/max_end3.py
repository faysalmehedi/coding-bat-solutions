#Given an array of ints length 3, figure out which is larger, 
#the first or last element in the array, 
#and set all the other elements to be that value. 
#Return the changed array.


def max_end3(nums):
	x = nums[0]
	y = nums[-1]
	if x > y:
		return [x,x,x]
	return [y,y,y]

	#alternative

	'''m = max(nums[0], nums[-1])
	nums[0] = m
	nums[1] = m
	nums[2] = m
	return nums'''

print(
max_end3([1, 2, 3]),
max_end3([11, 5, 9]),
max_end3([2, 11, 3]))