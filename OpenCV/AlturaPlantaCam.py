import imutils.contours
import cv2 
import cv2 as cv
from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep

#Tomar foto en raspberry
camera = PiCamera()
rawCapture = PiRGBArray(camera)
sleep(0.1)
camera.capture(rawCapture, format="bgr")
image = rawCapture.array

# Cover to grayscale and blur
greyscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
greyscale = cv2.GaussianBlur(greyscale, (7, 7), 0)
ret, thresh=cv.threshold(greyscale, 50, 255, cv.THRESH_BINARY)
# Resize and display the image (press key to exit)
resized_image2 = cv2.resize(thresh, (1280, 720))
cv2.imshow("Imagen binarizada", resized_image2)


# Detect edges and close gaps
canny_output = cv2.Canny(thresh, 50, 100)
# Resize and display the image (press key to exit)
resized_image3 = cv2.resize(canny_output, (1280, 720))
cv2.imshow("Imagen con canny", resized_image3)
canny_output = cv2.dilate(canny_output, None, iterations=1)
# Resize and display the image (press key to exit)
resized_image4 = cv2.resize(canny_output, (1280, 720))
cv2.imshow("Imagen dilatada", resized_image4)


# Get the contours of the shapes, sort l-to-r and create boxes
contours, hierarchies = cv2.findContours(canny_output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if len(contours) < 2:
    print("Couldn't detect two or more objects")
    exit(0)

(contours, _) = imutils.contours.sort_contours(contours)
contours_poly = [None]*len(contours)
boundRect = [None]*len(contours)
for i, c in enumerate(contours):
    contours_poly[i] = cv2.approxPolyDP(c, 3, True)
    boundRect[i] = cv2.boundingRect(contours_poly[i])

output_image = image.copy()
mmPerPixel = 16
 / boundRect[0][2]
print(boundRect[0][2])
print(mmPerPixel)
NumRec=0
IndiceRec=0
for i in range(0, len(contours)):

    # Too smol?
    if boundRect[i][2] < 100 or boundRect[i][3] < 100:
        continue

    # Create a boundary box
    cv2.rectangle(output_image, (int(boundRect[i][0]), int(boundRect[i][1])),
                  (int(boundRect[i][0] + boundRect[i][2]),
                  int(boundRect[i][1] + boundRect[i][3])), (0, 255, 0), 3)
    NumRec=NumRec+1
    IndiceRec=i
    print(boundRect[i],i)

PrimerRect = image.copy()
# Create a boundary box
cv2.rectangle(PrimerRect, (int(boundRect[0][0]), int(boundRect[0][1])),(int(boundRect[0][0] + boundRect[0][2]), int(boundRect[0][1] + boundRect[0][3])), (0, 255, 0), 3)
# Resize and display the image (press key to exit)
resized_imagePrimerRec = cv2.resize(PrimerRect, (1280, 720))
cv2.imshow("Primer rectangulo", resized_imagePrimerRec)

# Calculate the size of our plant
print('Rectangulos encontrados:',NumRec)
print(IndiceRec)
plantHeight = (boundRect[IndiceRec][3]) * mmPerPixel
print("Plant height is {0:.0f}mm".format(plantHeight))

# Resize and display the image (press key to exit)
resized_image = cv2.resize(output_image, (1280, 720))
cv2.imshow("Image", resized_image)
cv2.waitKey(0)
