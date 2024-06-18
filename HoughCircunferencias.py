import cv2
import numpy as np

img = cv2.imread('imagenes\circulo-motor.png', cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_blurred = cv2.medianBlur(gray, 5)

circles = cv2.HoughCircles(
    gray_blurred, 
    cv2.HOUGH_GRADIENT, dp=1, minDist=40, param1=100, param2=30, minRadius=30, maxRadius=42
)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
        cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)

cv2.imshow('Circulos detectados', img)
cv2.imwrite('CirculoDetectado.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
