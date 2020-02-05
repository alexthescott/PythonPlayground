""" big_diff.py Alex Scott 2020 
 taken from https://codingbat.com/prob/p184853

 Given an array of ints with at least 1 value,
 return the difference between the largest and smallest values
""" 

def big_diff_loop(nums):
	"""
	Parameters:
	list of ints, size > 0

	Returns:
	difference between max and min as int

	Why do we set max and min to none?
	"""
	max = None
	min = None
	for i in nums:
		if min == None or i < min:
			min = i
		if max == None or i > max:
			max = i
	return max - min

def big_diff_list_method(nums):
	"""
	Parameters:
	list of ints, size > 0

	Returns:
	difference between max and min as int

	Python's built in functions can make our life easier
	list documentation: https://bit.ly/2um6EKc
	"""
	return max(nums) - min(nums)

assert big_diff_list_method([2,42,33,6,8,12]) == 40
assert big_diff_loop([2,42,33,6,8,12]) == 40