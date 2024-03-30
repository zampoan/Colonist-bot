import numpy as np
import cv2 
import matplotlib.pyplot as plt

GREEN = (0, 255, 0)

# Load and convert to grayscale - less computationally expensive and more accurate
imgRGB = cv2.imread('colonist-ui.jpeg')
img = cv2.imread('colonist-ui.jpeg', cv2.IMREAD_GRAYSCALE)
template = cv2.imread('wheat.png', cv2.IMREAD_GRAYSCALE)

w,h = template.shape[::-1]

# Match template with image
result = cv2.matchTemplate(img, template, method=cv2.TM_CCOEFF)

# Filter out most likely points by threshold value
threshold = 0.8

#  Show location 
location = np.where(result >= threshold)

for pt in zip(*location[::-1]):
    cv2.rectangle(imgRGB, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

cv2.imwrite('result.png', imgRGB)
