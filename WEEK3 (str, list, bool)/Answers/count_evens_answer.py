""" count_evens_answer.py Alex Scott 
 taken from https://codingbat.com/prob/p189616

 Write a function which accepts a list of ints
 and returns the count of even ints
 """
temp = [2, 5, 6, 7, 3, 2, 1]

def count_evens(list):
	count = 0
	for item in list:
		if item % 2 == 0: count += 1
	return count

assert count_evens(temp) == 3