# -*- coding: utf-8 -*-
import cv2
import numpy as np

test_img = cv2.imread('fiverr.png')
test_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)

template = cv2.imread('five_template.png')
template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

w, h = template.shape[::-1]
# template = cv2.Canny(template, 50, 200)
# print(template)
result = cv2.matchTemplate(test_img, template, cv2.TM_CCOEFF_NORMED)
# print(result)
threshold = 0.15
loc = np.where(result >= threshold)

dollar_location = []

for pt in zip(*loc[::-1]):
	dollar_location.append(cv2.rectangle(test_img, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2))

print(len(dollar_location))

cv2.imshow('temple', test_img)

# Step 1: Smooth the image using a Gaussian filter to remove high frequency noise.
# Step 2: Compute the gradient intensity representations of the image.
# Step 3: Apply non-maximum suppression to remove “false” responses to to edge detection.
# Step 4: Apply thresholding using a lower and upper boundary on the gradient values.
# Step 5: Track edges using hysteresis by suppressing weak edges that are not connected to strong edges.


# test_img = cv2.imread('testeroni.png')
# # gray = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)
# # blurred = cv2.GaussianBlur(gray, (3, 3), 0)

# # canny
# tight = cv2.Canny(test_img, 225, 250)

# cv2.imshow("edge", tight)


cv2.waitKey(0)