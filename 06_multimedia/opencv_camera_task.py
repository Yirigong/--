from typing import Any
import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Camera open failed')
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame2 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame3 = cv2.Canny(frame,100,150)
    cv2.imshow('frame',frame)
    cv2.imshow('gray',frame2)
    cv2.imshow('edge',frame3)

    if cv2.waitKey(10)==13:
        break

cap.release()
cv2.destroyAllWindows()
