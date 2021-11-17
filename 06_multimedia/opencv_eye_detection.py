import cv2

eye_cascade = cv2.CascadeClassifier('./xml/eye.xml')
img = cv2.imread('genius.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = eye_cascade.detectMultiScale(gray)
eyes = eye_cascade.detectMultiScale(gray)

for(x, y, w, h) in faces:
    cv2.rectangle(img, (x,y),(x+w, y+h),(0,0,255),2)
    roi_color = img[y:y+h, x:x+w]
    roi_gray = gray[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    
cv2.imshow('result',img)

cv2.waitKey(0)

cv2.destroyAllWindows()


