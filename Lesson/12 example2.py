import numpy as np
import cv2 as cv


def nothingB(x):
    print("B" + str(x))


def nothingG(x):
    print("G" + str(x))


def nothingR(x):
    print("R" + str(x))



cv.namedWindow('image')

cv.createTrackbar('B', 'image', 0, 255, nothingB)
cv.createTrackbar('G', 'image', 0, 255, nothingG)
cv.createTrackbar('R', 'image', 0, 255, nothingR)

# creating a switch
switch = "color/gray"
cv.createTrackbar(switch, 'image', 0, 1, nothingB)

while 1:
    img = cv.imread('lena.jpg')

    pos = cv.getTrackbarPos('B', 'image')
    cv.putText(img, str(pos), (50, 150), cv.FONT_HERSHEY_SIMPLEX, 5, (0, 0, 255))

    k = cv.waitKey(1) & 0xFF

    if k == 27:
        break

    b = cv.getTrackbarPos('B', 'image')
    g = cv.getTrackbarPos('G', 'image')
    r = cv.getTrackbarPos('R', 'image')
    s = cv.getTrackbarPos(switch, 'image')

    if s == 0:
        img[:, 3] = [b]
    else:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.imshow('image', img)

cv.destroyAllWindows()
