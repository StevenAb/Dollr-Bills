import cv2
import numpy as np

img_rgb = cv2.imread('fiverr.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

# template = cv2.imread('five_dollar_full.png',0)
# w, h = template.shape[::-1]

# res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF)
# threshold = 0.2
# loc = np.where( res >= threshold)

# for pt in zip(*loc[::-1]):
#     cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 10)

ret, thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(img_rgb, contours, -1, (0, 255, 0), 3)

cv2.imshow('Detected',img_rgb)
cv2.waitKey(0)