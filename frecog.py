import os
import cv2
import numpy as np
import uuid
import PIL
from PIL import Image


def main():
	# import cascades
	face_cascade = cv2.CascadeClassifier('haar_cascade_face.xml')
	eye_cascade = cv2.CascadeClassifier('haar_cascade_eye.xml')

	# frame from webcam
	capture = cv2.VideoCapture(0)

	while True:
		ret, img = capture.read()
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, 1.3, 5)

		img_height = img.shape[0]
		img_width = img.shape[1]

		for (x, y, w, h) in faces:
			cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)

			roi = gray[y:y+h, x:x+w]

			# do eyes later

		cv2.imshow('img', img)

		k = cv2.waitKey(30) & 0xff
		if k == 27:
			cv2.destroyAllWindows()

main()