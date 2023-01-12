import imutils.contours
import cv2 
import cv2 as cv

def cam_altura(altura_referencia):
    #Tomar foto camara usb
    cam = cv2.VideoCapture(0)
    image = cam.read()[1]

    #cambiar a version deslavada
    #BGR to l*a*b
    lab=cv.cvtColor(image, cv.COLOR_BGR2LAB)
    #resized_lab = cv2.resize(lab, (640, 480))
    #cv2.imshow("LAB", resized_lab)
    l, a, b = cv2.split(lab)
    #resized_a = cv2.resize(a, (640, 480))
    #cv2.imshow('verde a magenta', resized_a)

    desenfoque = cv2.GaussianBlur(a, (7, 7), 0)
    ret, thresh=cv.threshold(desenfoque,122,255, cv.THRESH_BINARY)
    # Resize and display the image (press key to exit)
    #resized_image2 = cv2.resize(thresh, (640, 480))
    #cv2.imshow("Imagen binarizada", resized_image2)


    # Detect edges and close gaps
    canny_output = cv2.Canny(thresh, 50, 100)
    # Resize and display the image (press key to exit)
    #resized_image3 = cv2.resize(canny_output, (640, 480))
    #cv2.imshow("Imagen con canny", resized_image3)

    canny_output = cv2.dilate(canny_output, None, iterations=1)
    # Resize and display the image (press key to exit)
    #resized_image4 = cv2.resize(canny_output, (640, 480))
    #cv2.imshow("Imagen dilatada", resized_image4)


    # Get the contours of the shapes, sort l-to-r and create boxes
    contours, hierarchies = cv2.findContours(canny_output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) < 2:
        print("Couldn't detect two or more objects")
        plantHeight=0.0
        return plantHeight

    (contours, _) = imutils.contours.sort_contours(contours)
    contours_poly = [None]*len(contours)
    boundRect = [None]*len(contours)
    for i, c in enumerate(contours):
        contours_poly[i] = cv2.approxPolyDP(c, 3, True)
        boundRect[i] = cv2.boundingRect(contours_poly[i])

    output_image = image.copy()
    mmPerPixel = altura_referencia/ boundRect[0][2]
    print(boundRect[0][2])
    print(mmPerPixel)
    NumRec=0
    IndiceRec=0
    for i in range(0, len(contours)):
        # Too smol?
        if boundRect[i][2] < 50 or boundRect[i][3] < 50:
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
    #resized_imagePrimerRec = cv2.resize(PrimerRect, (640, 480))
    #cv2.imshow("Primer rectangulo", resized_imagePrimerRec)
   
    #cambiar a version deslavada
    #BGR to l*a*b
    #lab=cv.cvtColor(image, cv.COLOR_BGR2LAB)
    #resized_lab = cv2.resize(lab, (640, 480))
    #cv2.imshow("LAB", resized_lab)
    #l, a, b = cv2.split(lab)
    #resized_a = cv2.resize(a, (640, 480))
    #cv2.imshow('verde a magenta', resized_a)ontrados:',NumRec)
    print('Rectangulos encontrados:',NumRec)
    print(IndiceRec)
    plantHeight = (boundRect[IndiceRec][3]) * mmPerPixel
    print("Plant height is {0:.0f}mm".format(plantHeight))
    if NumRec==0:
        plantHeight=0.0
        return plantHeight
    elif NumRec==1:
        plantHeight=0.1
        return plantHeight
    else:
        # Resize and display the image (press key to exit)
        #resized_image = cv2.resize(output_image, (640, 480))
        #cv2.imshow("Image", resized_image)
        return plantHeight
