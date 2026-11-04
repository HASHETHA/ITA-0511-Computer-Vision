
import cv2
import numpy as np

# Read the image
img = cv2.imread('sc.jpg')

# Get image dimensions
rows, cols = img.shape[:2]

# Define four points in the original image
pts1 = np.float32([
    [100, 100],
    [400, 100],
    [100, 400],
    [400, 400]
])

# Define four corresponding points
pts2 = np.float32([
    [50, 50],
    [350, 100],
    [100, 350],
    [400, 400]
])

# Calculate perspective transformation matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# Apply perspective transformation
result = cv2.warpPerspective(img, matrix, (cols, rows))

# Display images
cv2.imshow('Original Image', img)
cv2.imshow('Perspective Transformation', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
