import cv2

# print("Read the image file")
# img = cv2.imread("Resources/kong_img.jpg")
# cv2.imshow("Output",img)
# cv2.waitKey(1000)

print("Read the video file")
# cap = cv2.VideoCapture("Resources/kong_video.mp4")
cap = cv2.VideoCapture(0) # webcam
cap.set(3,640)
cap.set(4,480)
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'): break
