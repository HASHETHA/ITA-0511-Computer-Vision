
import cv2

cap = cv2.VideoCapture('video.mp4')

fps = cap.get(cv2.CAP_PROP_FPS)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Normal Video", frame)
    cv2.waitKey(int(1000/fps))

    cv2.imshow("Slow Motion", frame)
    cv2.waitKey(int(2000/fps))

    cv2.imshow("Fast Motion", frame)
    cv2.waitKey(int(250/fps))

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
