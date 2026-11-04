# EXPERIMENT 2: Gaussian Blur
import cv2
img=cv2.imread("sc.jpg")
if img is None:
    print("Imange not found!")
else:
    print("Image found")
    blur_img = cv2.GaussianBlur(img, (9,9), 0)
    cv2.imshow("Original Image", img)
    cv2.imshow("Gaussian Blur", blur_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
