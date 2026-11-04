import cv2

img = cv2.imread('sc.jpg')

rotated = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
cv2.namedWindow("Rotated Image", cv2.WINDOW_NORMAL)

cv2.resizeWindow("Original Image", 500, 400)
cv2.resizeWindow("Rotated Image", 500, 400)

cv2.moveWindow("Original Image", 100, 150)
cv2.moveWindow("Rotated Image", 600, 150)

cv2.imshow("Original Image", img)
cv2.imshow("Rotated Image", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()