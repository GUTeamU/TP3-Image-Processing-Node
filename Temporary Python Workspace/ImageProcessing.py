import cv2 as cv
# import pyopencv as cv
import numpy as np
from matplotlib import pyplot as plt
import sys

img = cv.imread('Testface.jpg',0)
edges = cv.Canny(img,100,200)

print img
print edges
i=0
# for line in edges:
# 	i+=1
# 	sys.stdout.write(str(i) + ": ")
# 	sys.stdout.flush()
# 	for pixel in line:
# 		sys.stdout.write(str(pixel) + ", ")
# 		sys.stdout.flush()
# 	print " "