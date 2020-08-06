import cv2
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

ori = cv2.imread("graphical.jpg", 0)
img = cv2.cvtColor(ori, cv2.COLOR_GRAY2BGR)
rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
edges = cv2.Canny(img, 50, 150, apertureSize=3)
lines = cv2.HoughLines(edges, 1, np.pi / 180, 100)

#print(lines)

for line in lines:
    print(line)
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * a)
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * a)
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)





cv2.imshow("canny", edges)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

