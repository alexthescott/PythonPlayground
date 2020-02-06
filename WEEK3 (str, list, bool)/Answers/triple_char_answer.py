""" triple_char_answer.py Alex Scott 2020
 obviously influenced by https://codingbat.com/prob/p170842
"""

def triple_char(str):
	"""for a given string, return a new string with each char * 3

	Parameters: str
	Returns: a new string with each char * 3
	"""
	temp = ""
	for i in str:
		temp = temp + i * 3
	return temp

assert triple_char("oh-boy") == "ooohhh---bbboooyyy"