import os
import io
import cv2
from google.cloud import vision
from google.cloud.vision import types
import numpy as np

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= r'ServiceAccount.json'

client = vision.ImageAnnotatorClient()

FILE_NAME = 'text.png'
FOLDER_PATH = r'C:\Users\ppyan\Desktop\python\OCR\VisionAPIDemo'

File_object = open(r"output.txt","w+")

with io.open(os.path.join(FOLDER_PATH, FILE_NAME), 'rb') as image_file:
    content = image_file.read()

image = vision.types.Image(content=content)
response = client.text_detection(image=image)
texts = response.text_annotations
print('Texts:')
print(texts[1])

for text in texts:
    print('\n"{}"'.format(text.description.encode("utf-8")))

    File_object.write('\n"{}"'.format(text.description.encode("utf-8")))

    vertices = (['({},{})'.format(vertex.x, vertex.y)
                for vertex in text.bounding_poly.vertices])

    print('bounds: {}'.format(','.join(vertices)))
