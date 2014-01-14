import cv2 as cv
# import pyopencv as cv
import numpy as np
from matplotlib import pyplot as plt


# define 0 as lower pen
# define 1 as raise pen
	
def createInstructions(image, colour=255):
	pixels_visited = {}
	set_of_instructions = []
	x=0
	for line in image:
		
		y=0
		# sys.stdout.write(str(i) + ": ")
		# sys.stdout.flush()
		for pixel in line:
			
			if ((x,y) not in pixels_visited):
				pixels_visited[(x,y)] = True
				if(pixel>=colour):
					instructions = [(x,y), 0]
					pen_state = 0
					pen_state = processLine(x, y, instructions, pen_state, pixels_visited, image, colour)
					set_of_instructions.append(instructions)
			y+=1
		x+=1
	return set_of_instructions
	
def processLine(x, y, instructions, pen_state, pixels_visited, image, colour):
	
	pState = pen_state
	
	# X #
	# o #
	# # #
	pState = checkDirection(x, y, -1, 0, instructions, pState, pixels_visited, image, colour)
	
	# # X
	# o #
	# # #
	pState = checkDirection(x, y, -1, 1, instructions, pState, pixels_visited, image, colour)


	# # #
	# o X
	# # #
	pState = checkDirection(x, y, 0, 1, instructions, pState, pixels_visited, image, colour)

	
	# # #
	# o #
	# # X
	pState = checkDirection(x, y, 1, 1, instructions, pState, pixels_visited, image, colour)

	
	# # #
	# o #
	# X #
	pState = checkDirection(x, y, 1, 0, instructions, pState, pixels_visited, image, colour)

	
	# # #
	# o #
#	X # #
	pState = checkDirection(x, y, 1, -1, instructions, pState, pixels_visited, image, colour)

	
	# # #
#	X o #
	# # #
	pState = checkDirection(x, y, 0, -1, instructions, pState, pixels_visited, image, colour)

	
#	X # #
	# o #
	# # #
	pState = checkDirection(x, y, -1, -1, instructions, pState, pixels_visited, image, colour)

		
	if(instructions[len(instructions)-1] != 1):
		instructions.append(1)
	return 1
	
def checkDirection(x, y, x_direction, y_direction, instructions, pState, pixels_visited, image, colour):
	if(((x + x_direction, y + y_direction) not in pixels_visited) and image[x + x_direction][y + y_direction]>=colour):
		if(pState==1):
			instructions.append((x,y))
			instructions.append(0)
			pState = 0
		instructions.append((x + x_direction, y + y_direction))
		pixels_visited[(x + x_direction, y + y_direction)] = True
		pState = processLine(x + x_direction, y + y_direction, instructions, pState, pixels_visited, image, colour)
	pixels_visited[(x + x_direction, y + y_direction)] = True
	return pState
	

img = cv.imread('circle.jpg',0)
edges = cv.Canny(img,100,200)


print img
print edges
instructions = createInstructions(img, 240)
print "finish processing edges"

for instruction in instructions:
	print instruction
# for instruction in instructions:
# 	previous_point = -1
# 	for point in instruction:
# 		current_point = point
# 		if(current_point==0):
# 			continue
# 		elif(current_point==1):
# 			previous_point = -1
# 		elif(previous_point == -1):
# 			previous_point = point		
# 		else:
# 			print [previous_point[0], current_point[0]], [previous_point[1], current_point[1]]
# 			line = plt.plot([previous_point[0], current_point[0]], [previous_point[1], current_point[1]])
# 			plt.setp(line, color='r', linewidth=5.0)
		
# plt.show()
