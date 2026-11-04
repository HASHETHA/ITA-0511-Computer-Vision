
# EXPERIMENT 3: Canny Edge Detection

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

    # 4. Apply Canny Edge Detection
    edges = cv2.Canny(gray_img, 100, 200)

    # 5. Display original and edge images
    cv2.imshow("Original Image", img)
    cv2.imshow("Canny Edge Detection", edges)

    # 6. Wait for key press
    cv2.waitKey(0)

    # 7. Close all windows
    cv2.destroyAllWindows()
