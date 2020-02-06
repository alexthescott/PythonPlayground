""" given_str_functions.py Alex Scott 2020
 batteries are included and can be found @:
 	https://docs.python.org/2.5/lib/string-methods.html

 functions included in this file
	 str.count()
	 str.islower() and str.isupper()
	 str.split()
	 str.find()
"""

# str.count() returns the number of instances of str subsection
assert "hello, my name is Alex".count("Alex") == 1
assert "42 is everything".count("42 is everything") == 1
assert "hungry for apples?".count("p") == 2

# str.islower() only true of all chars are lowercase
assert "this is how i text my peeps lol".islower() == True
assert "THIS IS HOW I SCREAM INTO MY PILLOW".isupper() == True

# str.split() splits a string at a given character, returns a list of strings
assert "woah this is a list now".split() == ["woah", "this", "is", "a", "list", "now"]
assert "I#hate#the#space#bar#hashtag#blessed".split("#") == ["I", "hate", "the", "space", "bar", "hashtag", "blessed"]

# str.find() returns the first index in the str where substring is found
assert "it's just a flesh wound".find("wound") == 18
assert "Wubba lubba dub dub".find("l") == 6