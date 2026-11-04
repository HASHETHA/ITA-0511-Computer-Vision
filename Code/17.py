
import cv2

# Read the original image
img = cv2.imread('sc.jpg')

# Create a copy of the original image
watermarked = img.copy()

# Add watermark text
cv2.putText(
    watermarked,
    'MY WATERMARK',
    (50, 100),
    cv2.FONT_HERSHEY_SIMPLEX,
    2,
    (0, 0, 255),
    3
)

# Display original and watermarked images
cv2.imshow('Original Image', img)
cv2.imshow('Watermarked Image', watermarked)

cv2.waitKey(0)
cv2.destroyAllWindows()
