import numpy as np
import cv2

img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')

print(img.shape) # tuple containing rows, columns, and channels
print(img.size) # returns total number of pixels
print(img.dtype) # returns image datatype obtained

# img[:,:,2] = 0 # makes all red pixels zero

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

dst = cv2.addWeighted(img, .9, img2, .1, 0)

cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
