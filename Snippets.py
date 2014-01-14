# Open CV tutorial to do canny edge detection
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Images are held as an array of arrays. It is of the format img[row][column]
img = cv.imread('lewis.jpg',0)
edges = cv.Canny(img,50,200)

plt.subplot(121)
plt.imshow(img,cmap = 'gray')
plt.title('Original Image')
plt.xticks([])
plt.yticks([])
plt.subplot(122)
plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image')
plt.xticks([])
plt.yticks([])

plt.show()

# Shows the image held in img with the title of window "image" until you press 0
cv.imshow("image", img)
cv.waitKey(0)

# Saves an image
cv.imwrite('01.png',img)

# To get openCV on Ubuntu
sudo apt-get install libopencv-dev
