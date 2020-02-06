""" spam_eggs_1_n_answer.py Alex Scott 2020
 if perfectly divisable by 2, print spam
 if perfectly divisable by 5, print eggs
 if perfectly divisable by 2 and 5, print spam and eggs
 else print the int 

 two versions, to kinds of loops
 """

# For Loop Version
def spam_and_eggs_for(n):
	for i in range(1, n):
		if i % 5 == 0 and i % 2 == 0: 
			print("spam and eggs")
		elif i % 5 == 0: 
			print("spam")
		elif i % 2 == 0: 
			print("eggs")
		else: print(i)

def spam_and_eggs_while(n):
	i = 1
	while i < n:
		if i % 5 == 0 and i % 2 == 0: 
			print("spam and eggs")
		elif i % 5 == 0: 
			print("spam")
		elif i % 2 == 0: 
			print("eggs")
		else: 
			print(i)
		i += 1

spam_and_eggs_for(42)
