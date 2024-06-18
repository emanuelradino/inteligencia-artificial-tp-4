import cv2
import numpy as np

img = cv2.imread('imagenes\motor-recta.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

lineas = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=150, maxLineGap=10)

for linea in lineas:
    x1, y1, x2, y2 = linea[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)


cv2.imshow('LineaMotor', img)
cv2.imwrite('LineaMotor.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
