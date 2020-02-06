""" first_half_answer.py Alex Scott 2020
 taken from https://codingbat.com/prob/p107010
 
 Write a function which returns the first half of a string
 Assume we want the floor (don't include middle character of odd size string)
 """

def first_half(word):
	"return just the first half of string"
	length = int(len(word) / 2)
	return word[0:length]
	
assert first_half("HelloThere") == "Hello"

# but hey look this function also works for lists!
assert first_half([1,2,3,4,5,6]) == [1,2,3]