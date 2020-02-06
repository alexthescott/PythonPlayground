""" enough_bricks_answer.py Alex Scott 2020 
 taken from https://codingbat.com/prob/p118406

 Params: small, big, goal

 Small bricks are 1 unit long
 Big bricks are 5 units long
 
 Return:
 True if we can build goal length
 False if we cannot

 two solutions presented
 	once with loops (alright)
 	once without loops 🎉

 """

def enough_bricks_loop(small, big, goal):
  while goal >= 5 and big > 0:
  	goal -= 5
  	big -= 1
  while goal > 0 and small > 0:
  	goal -= 1
  	small -= 1
  return goal == 0 

def enough_bricks_simple(small, big, goal):
	if big * 5 >= goal: 
    return small >= goal % 5
	else: 
    return small >= goal - big * 5
	
assert enough_bricks_simple(1,1,7) == False # We are missing one block of size 1
assert enough_bricks_loop(4,3,19) == True # We have exactly enough blocks