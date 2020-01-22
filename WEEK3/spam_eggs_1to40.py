""" spam_eggs_1to40.py Alex Scott 2020
 if perfectly divisable by 2, print spam
 if perfectly divisable by 5, print eggs
 if perfectly divisable by 2 and 5, print spam and eggs
 else print the int """


for i in range(1, 41):
	if i % 5 == 0 and i % 2 == 0: print("spam and eggs")
	elif i % 5 == 0: print("spam")
	elif i % 2 == 0: print("eggs")
	else: print(i)
