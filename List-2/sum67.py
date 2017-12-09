#Return the sum of the numbers in the array, 
#except ignore sections of numbers starting with a 6 and 
#extending to the next 7 (every 6 will be followed by at least one 7). 
#Return 0 for no numbers.

def sum67(nums):
	tot = 0
	found = False
	for i in range(len(nums)):
		if nums[i] == 6:
			found = True
		if not found:
			tot += nums[i]
		if nums[i] == 7 and found:
			found = False
	return tot



print(
sum67([1, 2, 2]),
sum67([1, 2, 2, 6, 99, 99, 7]),
sum67([1, 1, 6, 7, 2]))