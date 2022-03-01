import numpy as np
import cv2

img = cv2.imread("Resources/ipad.jpg")
img = cv2.resize(img, (500,500))
width, height = 400,400
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOuput = cv2.warpPerspective(img, matrix, (width, height))


cv2.imshow("IPad", img)
cv2.imshow("Output", imgOuput)
cv2.waitKey(0)