""" index_of_capitals.py Alex Scott 2020 """

def index_of_capitals(word):
	"""Given a string, return a list of capital char indexes"""
	indexList = []
	for i in range(len(word)):
		if word[i].isupper(): indexList.append(i)
	return indexList

assert (index_of_capitals("DRsmooshSIRCharles") == [0,1,8,9,10,11])