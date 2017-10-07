import cv2

img = cv2.imread('test3.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 105, 255, cv2.THRESH_BINARY)
cv2.imshow('threshold', thresh)
# thresh = cv2.GaussianBlur(thresh, (5,5), 0)
thresh = cv2.medianBlur(thresh, 5)
cv2.imshow('blur', thresh)


contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    print(len(approx))
    
    if len(approx) == 4:
    	print('square')
        cv2.drawContours(img,[cnt],0,(0,0,255),-1)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()