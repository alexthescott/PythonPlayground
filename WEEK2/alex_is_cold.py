# boolean logic, basic problem

# if it is 60 or below, and i do not have a jacket, i will not go outside
# if it is 40 or above, and i do have a jacket, i will go outside
# if it is raining i will never go outside
# write the function alex_is_cold(temp, jacket, rain) returning True if I would go outside, and False if I wouldn't

def alex_is_cold(temp, jacket, rain):
	if rain or temp < 40 or not jacket and temp < 60: return False
	elif temp < 60 and jacket or temp >= 60: return True
	
assert alex_is_cold(45, True, False) == True # it's cold, but it's not raining, and I have a jacket
assert alex_is_cold(35, True, False) == False # too cold for me, even for a jacket
assert alex_is_cold(65, False, False) == True # it's warm enough for no jacket
assert alex_is_cold(55, True, True) == False # it's raining, I'm not down for the outside world!
