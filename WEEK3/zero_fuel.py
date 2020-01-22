""" zero_fuel.py Alex Scott 2020 
 taken from https://www.codewars.com/kata/will-you-make-it/train/python 
 
 You were camping, and you realize that you are m miles from a pump
 You know that you're car's miles per gallon, and the number of gallons remaining 
 print True if you can make it, and False if you cannot """

mpg = 47
gallons = 4
m = 77
	
print(m <= mpg * gallons)