""" closest_points.py Alex Scott 2020
 tricky list iteration, alg analysis, enumerate(), nested for loops
 
 given a list of tuples representing points on the cartesian plane, find the two closest points in 
 a new function called closest_points
 distance = sqrt((x1 - x2)^2 + (y1 - y2)^2)
 assume only one pair of closest points, assume no overlapping points  
"""

points = [(1,2),(4,0),(5,3),(1,8),(4,5),(6,7)]

def closest_points(points):
	"""
	Use distance formula to find two closest points on a cartesian plane

	Parameters: 
	points: list of tuples containing (x, y) coordinates

	Returns:
	shortPoints: list of two tuples containing closest points
	"""

	dist = 0
	shortPoints = list()
	tempPoints = points
	
	for i, p, in enumerate(points):
		for j, q, in enumerate(points):
			if i < j:
				xDist = p[0] - q[0]
				yDist = p[1] - q[1] 
				tempDist = (xDist**2 + yDist**2)**(0.5)
				if dist == 0 or tempDist < dist:
					shortPoints.clear()
					shortPoints.append(p)
					shortPoints.append(q)
					dist = tempDist
		if i >= len(points): break

	print(dist)
	return shortPoints
	
print(closest_points(points))
