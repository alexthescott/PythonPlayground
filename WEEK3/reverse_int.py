""" reverse_int.py Alex Scott 
    given an int, return the int with all digits reversed 
"""

value = 12747323471894
temporary = ""
 
while value > 0:
	digit = value % 10
	temporary += str(digit) 
	value //= 10
	
print(temporary)
	
