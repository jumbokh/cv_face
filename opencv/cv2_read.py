import cv2

img = cv2.imread('orange.jpg')
cv2.imshow('My image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
