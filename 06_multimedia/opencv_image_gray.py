import cv2

img = cv2.imread('민우.jpg')
img2 = cv2.resize(img,(600,400))

gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('민우',gray)

cv2.waitKey(0)

cv2.destroyAllWindows()