import cv2
import numpy as np

def imgStack(img, size):
    img = cv2.resize(img, size)

    img = np.hstack((img,img))
    img = np.vstack((img,img))

    cv2.imshow(f"2x2 Stacked Image:({size[0]},{size[1]},3)",img)
    cv2.waitKey(0)

img = cv2.imread('Resources/kong_img.jpg')
size = (500, 500)
imgStack(img, size)

