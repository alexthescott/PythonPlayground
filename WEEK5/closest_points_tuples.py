""" closest_points_tuples.py Alex Scott 2020
 tricky tuple iteration, alg analysis, enumerate(), nested for loops
 
 given a tuple of tuples representing points on the cartesian plane, find the two closest points in 
 a new function called closest_points
 distance = sqrt((x1 - x2)^2 + (y1 - y2)^2)
 assume only one pair of closest points, assume no overlapping points  
"""

points = ((1,2),(4,0),(5,3),(1,8),(4,5),(6,7))

def closest_points_tuples(points):
	"""
	Use distance formula to find two closest points on a cartesian plane

	Parameters: 
	points: tuple of tuples containing (x, y) coordinates

	Returns:
	shortPoints: tuple of two tuples containing closest points

	Also we print the distance of the closest points for fun 😎
	"""

	dist = 0
	shortPoints = None
	for i, p, in enumerate(points):
		for j, q, in enumerate(points):
			if i < j:
				x1, y1 = p
				x2, y2 = q
				tempDist = ((x1 - x2)**2 + (y1 - y2)**2)**(0.5)
				if dist == 0 or tempDist < dist:
					shortPoints = (p, q)
					dist = tempDist
		if i >= len(points): break
	print(dist)
	return shortPoints
	
assert(closest_points_tuples(points)) == ((5, 3), (4, 5))
