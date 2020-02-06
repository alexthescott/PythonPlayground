""" enough_bricks_question.py Alex Scott 2020 
 taken from https://codingbat.com/prob/p118406

 Params: small, big, goal

 Small bricks are 1 unit long
 Big bricks are 5 units long
 Want to build goal units long
 
 Return:
 True if we can build goal length
 False if we cannot

 two solutions possible
 	once with loops (good)
 	once without loops (better)

 """

def enough_bricks(small, big, goal):
	
assert enough_bricks(1,1,7) == False # We are missing one block of size 1
assert enough_bricks(4,3,19) == True # We have exactly enough blocks