import cv2

cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)
cv2.namedWindow("Face Detection - Press q to Quit", cv2.WINDOW_NORMAL)
while True:

    ret, frame = cap.read()

    print("Frame read:", ret)

    if not ret:

        break

    cv2.imshow("Test", frame)

    if cv2.waitKey(1) == ord('q'):

        break

cap.release()

cv2.destroyAllWindows()

