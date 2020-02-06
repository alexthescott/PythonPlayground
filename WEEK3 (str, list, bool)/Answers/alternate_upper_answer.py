""" alternate_upper_answer.py Alex Scott 2020
 
 write a function which returns a str that alternates the 
 capitalization of each character, on the even index values

 newString = alternate_upper('apple')
 print(newString) -> 'ApPlE'

"""

def alternate_upper(word):
	newString = ""
	for i in range(0, len(word)):
		if i % 2 == 0: 
			newString += word[i].upper()
		else: 
			newString += word[i]
	return newString

assert alternate_upper("apple sauce") == "ApPlE SaUcE"