import cv2
from cv2 import ROTATE_90_CLOCKWISE

print(cv2.__version__)

image_name = './Cat03.jpg'
unchanged = cv2.imread(image_name, flags=cv2.IMREAD_UNCHANGED)
grayscale = cv2.imread(image_name, flags=cv2.IMREAD_GRAYSCALE)
color = cv2.imread(image_name, flags=cv2.IMREAD_COLOR) 

resized = cv2.resize(color, (100, 100))

rotated = cv2.rotate(resized, ROTATE_90_CLOCKWISE)

cv2.imwrite('./01edited.jpg', rotated)

cv2.imshow('IMAGE', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
