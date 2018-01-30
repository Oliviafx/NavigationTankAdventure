import math

# Used for the simulation
SMALL_DISTANCE = 0.01
SMALL_ANGLE = 0.01

def init_paths(waypoints):
    """ Initializes paths from input waypoints """
    paths = []
    if len(waypoints) < 2:
	return paths
    else:
	for i in range(1, len(waypoints)):
	    paths.append((waypoints[i-1], waypoints[i]))
	return paths

class Tank:
    def __init__(self, x, y, heading, waypoints):
	"""
	x = starting x-coordinate, in m (+x points to the right)
	y = starting y-coordinate, in m (+y points upwards)
	heading = starting header, in radians (0 is +x axis, increases counterclockwise)
	waypoints = same format as the bike format - list of waypoints
	            e.g. the path from 0,0 to 0,5 then to 7,6 would be passed in like this:
		    [(0, 0), (0, 5), (7, 6)]
	"""
	self.x = x
	self.y = y
	self.heading = heading
	self.waypoints = waypoints
	self.paths = init_paths(waypoints)

    def step(self, speed, yaw_dot):
	"""Perform one simulation step of this tank"""
	self.x += SMALL_DISTANCE * speed * math.cos(self.heading)
	self.y += SMALL_DISTANCE * speed * math.sin(self.heading)

	self.heading += yaw_dot * SMALL_ANGLE

    def get_nav_command(self):
	"""Returns the pair (speed, yaw_dot)"""
	speed = 1
	yaw_dot = 0.1
	return (speed, yaw_dot)
