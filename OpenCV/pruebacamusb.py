import cv2 

cam = cv2.VideoCapture(0)
image = cam.read()[1]
resized_image2 = cv2.resize(image, (640, 480))
cv2.imshow("Camara ejemplo", resized_image2)
cv2.waitKey(0)
