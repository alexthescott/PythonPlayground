""" def_functions.py Alex Scott 2020
 some function definition examples
"""

def recursive_print(n):
	""" given an int n, return a string of n and all values below until 0"""
	if n <= 0:
		return str(n) + " "
	else:
		return recursive_print(n - 1) + str(n) + " "

#print(recursive_print(42))

def silly_print(n):
	""" what the heck does print() return!? """
	result = print(n)
	print(result)

print(silly_print(42))