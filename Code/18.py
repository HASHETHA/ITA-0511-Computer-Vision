
import cv2

# Read the image
img = cv2.imread('sc.jpg')

# Select Region of Interest (ROI)
roi = img[100:300, 100:300]

# Create a copy of the original image
result = img.copy()

# Paste ROI into another location
result[350:550, 350:550] = roi

# Display images
cv2.imshow('Original Image', img)
cv2.imshow('Cropped Image', roi)
cv2.imshow('Copied and Pasted Image', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
