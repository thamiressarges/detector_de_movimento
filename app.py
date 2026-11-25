import cv2

cap = cv2.VideoCapture(0)

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    dif = cv2.absdiff(frame1, frame2)

    cinza = cv2.cvtColor(dif, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(cinza, (5,5), 0)

    _,thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

    cv2.imshow('Doferença', thresh)

    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()