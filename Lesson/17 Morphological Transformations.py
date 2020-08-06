import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('smarties.png', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((2, 2), np.uint8)

dilation = cv2.dilate(mask, kernel, iterations=2)
erosion = cv2.erode(mask, kernel, iterations=1)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

titles = ['image', 'mask', 'dilation', 'erosion', 'opening']
images = [img, mask, dilation, erosion, opening]

for i in range(5):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])

plt.show()