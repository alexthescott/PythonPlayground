""" dog_cat_answer.py Alex
 blatent rip off of https://codingbat.com/prob/p164876

 write a function which accepts a string, and returns true
 if the number of instances of 'cat' == number of instances of 'dog'

 once as the nieve implementation,
 another as the pythonic implementation
 """

# str.count() is what we should be using
def dog_cat_pythonic(word):
	return word.count("dog") == word.count("cat")

"""
 this makes me weep. Props if you made it this far, 
 but look how beautiful the implementation above is
"""
def dog_cat_nieve(word):
	bothCount = 0
	for i in range(len(word)):
		if word[i] == 'c' and 2 + i < len(word):
			if word[i+1] == 'a' and word[i+2] == 't':
				bothCount += 1
		elif word[i] == 'd' and 2 + i < len(word):
			if word[i+1] == 'o' and word[i+2] == 'g':
				bothCount -= 1
	return bothCount == 0

assert dog_cat_nieve("woah look, both a dog, and a cat at the same place") == True
assert dog_cat_pythonic("I wonder if the dog knows the cat, or if the dog has another friend") == False