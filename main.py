import numpy
import cv2
print cv2.__version__
img = cv2.imread('batman1.jpg', 0)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('grayscale_batman.png', img)
