
# EXPERIMENT 4: Histogram Equalization

import cv2

# 1. Read the image
img = cv2.imread("C:/Users/Hashetha/Documents/CV_Lab/sc.jpg")

# 2. Check whether image is loaded
if img is None:
    print("Image not found!")

else:
    print("Image found successfully!")

    # 3. Convert colour image into grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 4. Apply Histogram Equalization
    equalized_img = cv2.equalizeHist(gray_img)

    # 5. Display original and equalized images
    cv2.imshow("Original Grayscale Image", gray_img)
    cv2.imshow("Histogram Equalized Image", equalized_img)

    # 6. Wait for key press
    cv2.waitKey(0)

    # 7. Close all windows
    cv2.destroyAllWindows()
