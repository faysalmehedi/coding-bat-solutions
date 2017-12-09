#We want to make a row of bricks that is goal inches long. 
#We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
#Return True if it is possible to make the goal by choosing from the given bricks. 
#This is a little harder than it looks and can be done without any loops. 
#See also: Introduction to MakeBricks

def make_bricks(small, big, goal):
	if goal >= big * 5:
		remainder = goal - (big * 5)
	else:
		remainder = goal % 5
	if small >= remainder:
		return True
	return False

print(
make_bricks(3, 1, 8),
make_bricks(3, 1, 9),
make_bricks(3, 2, 10))