""" dog_cat_question.py Alex
 blatent rip off of https://codingbat.com/prob/p164876

 write a function which accepts a string, and returns true
 if the number of instances of 'cat' == number of instances of 'dog'

 please lookup the function str.count(), or you'll have a bad time 🤮
 """

def dog_cat(word):

assert dog_cat("woah look, both a dog, and a cat at the same place") == True
assert dog_cat("I wonder if the dog knows the cat, or if the dog is alone...") == False