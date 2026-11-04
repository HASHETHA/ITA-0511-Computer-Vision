
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread('sc.jpg')

# Get image dimensions
rows, cols = img.shape[:2]

# Define three points in the original image
pts1 = np.float32([
    [50, 50],
    [200, 50],
    [50, 200]
])

# Define three corresponding points
pts2 = np.float32([
    [10, 100],
    [200, 50],
    [100, 250]
])

# Calculate affine transformation matrix
matrix = cv2.getAffineTransform(pts1, pts2)

# Apply affine transformation
result = cv2.warpAffine(img, matrix, (cols, rows))

# Display original and transformed images
cv2.imshow('Original Image', img)
cv2.imshow('Affine Transformation', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
