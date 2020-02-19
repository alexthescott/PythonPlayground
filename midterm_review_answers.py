""" midterm_review_answers.py Alex Scott 2020
More practice: 
	- Multiple Choice -> https://www.geeksforgeeks.org/python-multiple-choice-questions/
	- Function Definition -> https://codingbat.com/python
	- My MSI Examples -> https://github.com/alexthescott/PythonPlayground
	- Learn Python in X minutes! 📙 -> https://learnxinyminutes.com/docs/python3/
"""

""" Question 1 - Fill in the blank response ------------------------------------------------
 List all of the basic data types in Python, and give examples of each type
-int, float, str, bool

 How can we convert an int into a string
-typecasting, like str(42) 

 List all 7 basic variable operators, and their functions (+, -, etc.)
- +, -, /, *, //, %, **

 List all 9 logical operators
- >, <, >=, <=, ==, !=, and, or, not

 List the two kinds of loops
- For Loops, While Loops

 When might we want a for loop instead of a while loop?
- While iterating across a string or a list, or we know the number of iterations

 When might we want a while loop instead of a for loop?
- While True, while we don't know the number of iterations, or a multi-case loop condition

 What are the two use cases of in
- Iterate across list/str, or check if elem in list/str. ex// For i in str... if char in 'aeiouAEIOU' 

 What is a list?
-collection of data stored sequentially, and without preference for a data type

 What is a tuple?
-colllection of immutable data stored sequentially, and without preference for a data type

 How do lists and tuples differ?
-lists are mutable, tuples are not. Lists have more functions available ex// list.append()

 How can we index a list?
-list[int]

 How can we slice a list/string, and what happens if we index a slice out of bounds?
-string[0:len(string)] by default. And yes we can index out of bounds on a slice
""" 

""" Question 2 - Multiple Choice -------------------------------------------""" """  
1) What is printed to the output? """
a = "meaning of life"
b = 42 
print(a + b)
"""
 a) 42 meaning of life
-b) error
 c) meaning of life 42 
 d) meaning of life42

 str and int cannot be added. Maybe print(a + str(b))
""" """ 
2) What is printed to the output? """
listA = [2,4,(3,4),10,12]
b = listA[2]
b = b * 2
print(listA)
"""
-a) [2,4,(3,4),10,12]
 b) [2,4,(6,8),10,12]
 c) [2,4,(3,4,3,4),10,12]
 d) [2,4,(3,4,6,8),10,12]

 tuples are immutable. Maybe listA[2] = (6,8)
""" """
3) What is printed to the output? """
listA = ['ringo','paul', 42, True]
c = listA[0][-1]
c = c * 2
print(c)
"""
 a) ringoringo
 b) ringo
-c) oo
 d) rr

 listA[0] == 'ringo'
 listA[0][-1] grabs the last char from 'ringo'
""" """
4) What is printed to the output? """
listA = [3,6,9,12]
listA = listA * 2
print(listA)
"""
 a) [6,12,19,24]
 b) [3,6,9,12,6,12,19,24]
 c) [3,6,9,12]
-d) [3,6,9,12,3,6,9,12]

 list * int repeats each list entry int times
""" """
5) What is printed to the output? """
def first_half(word):
 	length = int(len(word / 2))
 	return word[0: length]
print(first_half("racecar"))
"""
 a) racecar
 b) race
 c) rac
-d) error

trying to grab len(word / 2), which is impossible
""" """
6) What is printed to the output? """
def first_half(word):
 	length = int(len(word) / 2)
 	return word[0: length]
print(first_half("racecar"))
"""
 a) racecar
 b) race
-c) rac
 d) error

 cuts off the char at index 3
""" """
7) What is printed to the output? """
def first_half(word):
 	length = int(len(word) / 2)
 	return word[0: length]
print(first_half([1,2,3,4,5]))
"""
 a) [1,2,3,4,5]
 b) [1,2,3]
-c) [1,2]
 d) error

 also works for lists!
""" """
8) What is printed to the output? """
def first_half(word):
 	length = int(len(word) / 2)
 	return word[0: length]
print(first_half((1,2,3,4,5)))
"""
 a) (1,2,3,4,5)
 b) (1,2,3)
-c) (1,2)
 d) error

 also works for tuples!
""" """
9) How many times does this program print "here!"? """
for i in range(10):
	if i % 2 == 0:
		print(i, end = ' ')
	else:
		print("here", end = ' ')

"""
 a) 3 times
 b) 4 times
-c) 5 times
 d) 0 times

 0-9 has 5 odd numbers
""" """ 
10) What is printed to the output? """
x = -42
if x < 0: print("Less than zero")
if x < 10: print("Less than 10")
if x < 20: print("Less than 20")
elif x < 42: print("Less than 42")
"""
 a) Less than zero
 b) Less than 10
-c) Less than zero
    Less than 10
    Less than 20
 d) Less than zero
    Less than 10

 no elif means we keep checking the next if condition
""" """ 
11) What is the expected output? """
for i in range(6):
	print(i)
else:
	print("We're Done!")

"""
 a) 0-6, then We're Done!
 b) error
-c) 0-5, We're Done! each loop iteration
 d) 0-6, We're Done! each loop iteration

 It should be noted that you can also have a while else block
""" """  
12) What is printed to the output? """
string = "Hello World!"
x = string[30]
print(x)
"""
 a) !
 b) r
 c) rld!
-d) error
""" """  
12) What is printed to the output? """
string = "Hello World!"
x = string[-1:30]
print(x)
"""
-a) !
 b) H
 c) W
 d) Hello World!
""" """  
13) What is printed to the output? """
string = "Hello World!"
x = string[:42]
print(x)
"""
 a) !
 b) H
 c) W
-d) Hello World!
""" """  
14) What is printed to the output? """
for i in range(20, 13, -4):
	print(i, end=' ')
"""
 a) 21 17 13
 b) 13 17 21
 c) 13 17
-d) 20 16
""" """  
15) What is printed to the output? """
for i in range(2):
 	for j in range(2):
 		print(i, end = ' ')
"""
 a) 0 1
-b) 0 0 1 1 
 c) 0 1 2 0 1 2
 d) 0 1 0 1
""" """  
15) Single line conditional assignment """
myFruit = 'apple'
fruits = ['banana','orange','apple','kiwi']
inFruits = True if myFruit in fruits else False
print(inFruits)
"""
-a) True
 b) False
 c) error
 d) None
""" """
16) Why is Python called Python? """
"""
 a) the author loved snakes
 b) the author hated snakes
-c) the author loved the TV show 'Monty Python'
 d) because snakes invented programming

"""

""" Question 3 - Function Definition -------------------------------------------""" """
 You show up to the midterm early, and want to go on a stroll. A block takes 1 minute to walk, and 
 you have 10 minutes until your midterm starts.

 Write a function which accepts a list arbitrary length. 
 The list will contain 'n', 's', 'e', 'w', the block directions you can travel.

 Only return true if we take a 10 minute stroll, and end up where we began 

 Hint: Think about how we can keep track of directions, and time elapsed. also list.count() is everything...

 ex//
 	midtermStroll(['n', 'n', 'e', 'w', 's', 's', 'e', 'e', 'w', 'w']) -> True
 	midtermStroll([n, n, e, w, s, s, e, e, s, s]) -> False

SOLUTION:

def midtermStroll(walk):
	return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')

or

def midtermStroll(walk):
	if len(walk) == 10:
		if walk.count('n') == walk.count('s'):
			if walk.count('e') == walk.count('w'):
				return True
	return False

 You want to write a small program to find the two closest points given a plot on the x, y graph

 Write a function which accepts a list containing (x, y) tuples. Assume points are unique.
 Return a list of the two tuples closest to each other

 I encourage you to try to solve this problem on paper, with a list of your own creation. How can we compare
 every point to every other point without. You will need a well thought out nested loop

 ex//
 	closest_points([(1,2),(1,1),(3,7)]) == [(1,2),(1,2)]
 	closest_points([(1,2),(4,0),(5,3),(1,8),(4,5),(6,7)]) == [(4,5),(6,7)]

SOLUTION:
def closest_points(points):
	shortPoints = []
	dist = 0
	for i, p, in enumerate(points):
		for j, p, in enumerate(points):
			if i < j:
				xDist = p[0] - q[0]
				yDist = p[1] - q[1]
				tempDist = (xDist**2 + yDist**2)**(0.5)
				if dist == 0 or tempDist < dist:
					shortPoints = []
					shortPoints.extend([p,q])
	return shortPoints
"""

def midtermStroll(walk):
	if len(walk) == 10:
		if walk.count('n') == walk.count('s'):
			if walk.count('e') == walk.count('w'):
				return True
	return False

assert midtermStroll(['n', 'n', 'e', 'w', 's', 's', 'e', 'e', 'w', 'w']) == True

def closest_points(points):
	shortPoints = []
	dist = 0
	for i, p, in enumerate(points):
		for j, p, in enumerate(points):
			if i < j:
				xDist = p[0] - q[0]
				yDist = p[1] - q[1]
				tempDist = (xDist**2 + yDist**2)**(0.5)
				if dist == 0 or tempDist < dist:
					shortPoints = []
					shortPoints.extend([p,q])
	return shortPoints

assert(closest_points([(1,2),(4,0),(5,3),(1,8),(4,5),(6,7)]) == [(4,5),(6,7)])
