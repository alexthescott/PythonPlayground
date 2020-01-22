temp = [2, 5, 6, 7, 3, 2, 1]

def count_evens(list):
	count = 0
	for item in list:
		if item % 2 == 0: count += 1
	return count

print(count_evens(temp))