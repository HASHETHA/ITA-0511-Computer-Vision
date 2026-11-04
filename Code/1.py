
# EXPERIMENT 1: Read an Image and Convert It into Grayscale

import cv2

# 1. Read the image
img = cv2.imread("sc.jpg")

# 2. Check whether the image is loaded
if img is None:
    print("Image not found!")
else:
    print("Image found successfully!")

    # 3. Display image dimensions
    print("Image dimensions:", img.shape)

    # 4. Convert BGR image into grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 5. Display original and grayscale images
    cv2.imshow("Original Image", img)
    cv2.imshow("Grayscale Image", gray_img)

    # 6. Wait until a key is pressed
    cv2.waitKey(0)

    # 7. Close all image windows
    cv2.destroyAllWindows()
