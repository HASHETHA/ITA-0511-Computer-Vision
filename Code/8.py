
import cv2
import numpy as np

img = cv2.imread('cat.jpg')

kernel = np.ones((5, 5), np.uint8)
dilation = cv2.dilate(img, kernel, iterations=1)

cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
cv2.namedWindow("Dilated Image", cv2.WINDOW_NORMAL)

cv2.resizeWindow("Original Image", 500, 400)
cv2.resizeWindow("Dilated Image", 500, 400)

cv2.moveWindow("Original Image", 200, 150)
cv2.moveWindow("Dilated Image", 750, 150)

cv2.imshow("Original Image", img)
cv2.imshow("Dilated Image", dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()
