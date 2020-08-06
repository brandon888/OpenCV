import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

ori = cv2.imread('receipt 1.jpg')
height, width, _ = ori.shape
img = cv2.resize(ori, (width*2, height*2))
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# print(pytesseract.image_to_string(img))

text = pytesseract.image_to_string(img)
result = text.split("\n")

# Detecting Characters

imgHeight, imgWidth, _ = img.shape
boxes = pytesseract.image_to_boxes(img)

data = pytesseract.image_to_data(img)
print(data)

highest = imgHeight
highestText = ""

countColon = 0
yDate = 0

adrContact = [""]

yText=0

for x, b in enumerate(data.splitlines()):
    if x != 0:
        countColon = 0
        b = b.split()
        #(b)  # prints x, y,   width, height
        if len(b) == 12:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 2)
            #cv2.putText(img, b[0], (x, imgHeight - y + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (50, 50, 255), 1)

            yText = int(b[7])
            if yText < highest:
                highest = yText
                highestText = b[11]


            for character in b[11]:
                if character == ":":
                    countColon = countColon + 1
                    if countColon > 1:
                        yDate = int(b[7])


# for x, b in enumerate(data.splitlines()):
#     if x != 0:
#         b = b.split()
#         if len(b) == 12:
#             if int(b[7]) > yText & int(b[7]) < yDate:
#                 adrContact.append(str(b[11]))



indexOfDate = 0


for x, word in enumerate(result):
    if word.count(":") > 1:
        indexOfDate = x

companyInformation = []
for e in result:
    if result.index(e) < indexOfDate & len(e) > 0:
        companyInformation.append(e)

print("Company Information: ")
print(companyInformation)










cv2.imshow('Result', img)
cv2.waitKey(0)
