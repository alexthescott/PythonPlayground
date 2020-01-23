""" Meaning_Of_Life_Input.py Alex Scott 2020

 Ask user for an int
 Print it's difference with 42, the meaning of life
 	"You are n units away from the meaning of life"

 use the abs() function to return a positive difference 
"""

guess = input("Which integer is the meaning of life?\n")
guess = int(guess)
difference = abs(42 - guess) 
print("You are", difference, "units away from the meaning of life")
