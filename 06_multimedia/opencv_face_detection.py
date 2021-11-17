import cv2

face_cascade = cv2.CascadeClassifier('./xml/face.xml')
img = cv2.imread('genius.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray)

for(x, y, w, h) in faces:
    cv2.rectangle(img, (x,y),(x+w, y+h),(0,0,255),2)

cv2.imshow('result',img)

cv2.waitKey(0)

cv2.destroyAllWindows()


