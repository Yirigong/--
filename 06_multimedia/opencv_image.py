import cv2

img = cv2.imread('민우.jpg')
img2 = cv2.resize(img,(600,400))

cv2.imshow('민우',img2)




cv2.waitKey(0)

cv2.destroyAllWindows()