""" car_trip_home_answer.py Alex Scott 2020 
 taken from https://www.codewars.com/kata/will-you-make-it/train/python 
 
 You were camping, and you realize that you are m miles from a pump
 You know that you're car's miles per gallon, and the number of gallons remaining 
 
 Write a function which returns the bool value of 'can I came it home'
 True if we can make it to the pump
 False if we cannot make it to the pump

"""

def car_trip_home(m, mpg, g):
	return m <= mpg * g

assert car_trip_home(48, 11, 5) == True
assert car_trip_home(48, 11, 4) == False