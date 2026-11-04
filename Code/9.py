
import cv2

img = cv2.imread('cat.jpg')

bigger = cv2.resize(img, None, fx=1.5, fy=1.5)
smaller = cv2.resize(img, None, fx=0.5, fy=0.5)

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Bigger", cv2.WINDOW_NORMAL)
cv2.namedWindow("Smaller", cv2.WINDOW_NORMAL)

cv2.resizeWindow("Original", 400, 300)
cv2.resizeWindow("Bigger", 400, 300)
cv2.resizeWindow("Smaller", 400, 300)

cv2.moveWindow("Original", 100, 100)
cv2.moveWindow("Bigger", 550, 100)
cv2.moveWindow("Smaller", 1000, 100)

cv2.imshow("Original", img)
cv2.imshow("Bigger", bigger)
cv2.imshow("Smaller", smaller)

cv2.waitKey(0)
cv2.destroyAllWindows()
