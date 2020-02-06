""" index_of_capitals_answer.py Alex Scott 2020 

 Write a function which accepts a str, and returns a list of indexes of capital characters
"""

def index_of_capitals(word):
	"""Given a string, return a list of capital char indexes"""
	indexList = []
	for i in range(len(word)):
		if word[i].isupper(): indexList.append(i)
	return indexList

assert (index_of_capitals("DRsmooshSIRCharles") == [0,1,8,9,10,11])