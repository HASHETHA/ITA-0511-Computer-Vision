
import cv2
import matplotlib.pyplot as plt

# Read the input image
img = cv2.imread('sc.jpg')

# Check whether image is loaded
if img is None:
    print("Image not found")
else:
    # Define color channels
    colors = ('b', 'g', 'r')
    labels = ('Blue', 'Green', 'Red')

    # Analyze histogram for each color channel
    plt.figure(figsize=(8, 5))

    for i, color in enumerate(colors):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])

        plt.plot(hist, color=color, label=labels[i])
    plt.title("Color Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Number of Pixels")
    plt.legend()
    plt.xlim([0, 256])

    plt.show()