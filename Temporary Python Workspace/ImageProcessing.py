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
		x+=1
		y=0
		# sys.stdout.write(str(i) + ": ")
		# sys.stdout.flush()
		for pixel in line:
			y+=1
			if ((x,y) not in pixels_visited):
				pixels_visited[(x,y)] = True
				if(pixel==colour):
					instructions = [(x,y), 0]
					pen_state = 0
					pen_state = processLine(x, y, instructions, pen_state, pixels_visited, image, colour)
					set_of_instructions.append(instructions)
	return set_of_instructions
	
def processLine(x, y, instructions, pen_state, pixels_visited, image, colour):
	
	pState = pen_state
	
	# X #
	# o #
	# # #
	if(((x-1,y) not in pixels_visited) and image[x-1][y]==colour):
		if(pState==1):
			instructions.append((x,y))
			instructions.append(0)
			pState = 0
		instructions.append((x-1, y))
		pixels_visited[(x-1, y)] = True
		pState = processLine(x-1, y, instructions, pState, pixels_visited, image, colour)
	pixels_visited[(x-1, y)] = True
	
	# # X
	# o #
	# # #
	if(((x-1,y+1) not in pixels_visited) and image[x-1][y+1]==colour):
		if(pState==1):
			instructions.append((x,y))
			instructions.append(0)
			pState = 0
		instructions.append((x-1, y+1))
		pixels_visited[(x-1, y+1)] = True
		pState = processLine(x-1, y+1, instructions, pState, pixels_visited, image, colour)
	pixels_visited[(x-1, y+1)] = True

	# # #
	# o X
	# # #
	if(((x,y+1) not in pixels_visited) and image[x][y+1]==colour):
		if(pState==1):
			instructions.append((x,y))
			instructions.append(0)
			pState = 0
		instructions.append((x, y+1))
		pixels_visited[(x, y+1)] = True
		pState = processLine(x, y+1, instructions, pState, pixels_visited, image, colour)
	pixels_visited[(x, y+1)] = True
	
	# # #
	# o #
	# # X
	if(((x+1,y+1) not in pixels_visited) and image[x+1][y+1]==colour):
		if(pState==1):
			instructions.append((x,y))
			instructions.append(0)
			pState = 0
		instructions.append((x+1, y+1))
		pixels_visited[(x+1, y+1)] = True
		pState = processLine(x+1, y+1, instructions, pState, pixels_visited, image, colour)
	pixels_visited[(x+1, y+1)] = True
	
	# # #
	# o #
	# X #
	if(((x+1,y) not in pixels_visited) and image[x+1][y]==colour):
		if(pState==1):
			instructions.append((x,y))
			instructions.append(0)
			pState = 0
		instructions.append((x+1, y))
		pixels_visited[(x+1, y)] = True
		pState = processLine(x+1, y, instructions, pState, pixels_visited, image, colour)
	pixels_visited[(x+1, y)] = True
	
	# # #
	# o #
#	X # #
	if(((x+1,y-1) not in pixels_visited) and image[x+1][y-1]==colour):
		if(pState==1):
			instructions.append((x,y))
			instructions.append(0)
			pState = 0
		instructions.append((x+1, y-1))
		pixels_visited[(x+1, y-1)] = True
		pState = processLine(x+1, y-1, instructions, pState, pixels_visited, image, colour)
	pixels_visited[(x+1, y-1)] = True
	
	# # #
#	X o #
	# # #
	if(((x,y-1) not in pixels_visited) and image[x][y-1]==colour):
		if(pState==1):
			instructions.append((x,y))
			instructions.append(0)
			pState = 0
		instructions.append((x, y-1))
		pixels_visited[(x, y-1)] = True
		pState = processLine(x, y-1, instructions, pState, pixels_visited, image, colour)
	pixels_visited[(x, y-1)] = True
	
#	X # #
	# o #
	# # #
	if(((x-1,y-1) not in pixels_visited) and image[x-1][y-1]==colour):
		if(pState==1):
			instructions.append((x,y))
			instructions.append(0)
			pState = 0
		instructions.append((x-1, y-1))
		pixels_visited[(x-1, y-1)] = True
		pState = processLine(x-1, y-1, instructions, pState, pixels_visited, image, colour)
	pixels_visited[(x-1, y-1)] = True
		
	if(instructions[len(instructions)-1] != 1):
		instructions.append(1)
	return 1
	

img = cv.imread('Testface.jpg',0)
edges = cv.Canny(img,100,200)



print img
print edges
instructions = createInstructions(edges)
print "finish processing edges"
#plt.plot([0.0,10.00], [0.0,10.0])
#plt.show()
plt.plot(instructions[0][0][0], instructions[0][2][0], instructions[0][0][1], instructions[0][2][1])
plt.show()
for instruction in instructions:
	previous_point = -1
	for point in instruction:
		current_point = point
		if(current_point==0):
			continue
		elif(current_point==1):
			previous_point = -1
		elif(previous_point == -1):
			previous_point = point		
		else:
			print [previous_point[0], current_point[0]], [previous_point[1], current_point[1]]
			line = plt.plot([previous_point[0], current_point[0]], [previous_point[1], current_point[1]])
			plt.setp(line, color='r', linewidth=5.0)
		
plt.show()
