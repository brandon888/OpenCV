import numpy as np
import cv2
import pytesseract



pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'


img = cv2.imread("graphs.jpg", 0)
imgR = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
inverted = cv2.bitwise_not(imgR)

thresh = cv2.threshold(inverted, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

coords = np.column_stack(np.where(thresh > 0))
angle = cv2.minAreaRect(coords)[-1]

if angle < -45:
    angle = -(90 + angle)
else:
    angle = -angle

(h, w) = inverted.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated = cv2.warpAffine(inverted, M, (w, h), flags = cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

cv2.putText(rotated, "Angle: {:.2f} degrees".format(angle), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
print(pytesseract.image_to_string(rotated))

cv2.imshow("graph", inverted)
cv2.imshow("rotated", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
