# TODO first step is to import the opencv module which is called 'cv2'
import cv2
from cv2 import ROTATE_90_CLOCKWISE

# TODO check the opencv version
print(cv2.__version__)

# TODO load an image with image reading modes using 'imread'
# cv2.IMREAD_UNCHANGED  - If set, return the loaded image as is (with alpha
#                         channel, otherwise it gets cropped). Ignore EXIF
#                         orientation.
# cv2.IMREAD_GRAYSCALE  - If set, always convert image to the single channel
#                         grayscale image (codec internal conversion).
# cv2.IMREAD_COLOR      - If set, always convert image to the 3 channel BGR
#                         color image.
image_name = './Cat03.jpg'
unchanged = cv2.imread(image_name, flags=cv2.IMREAD_UNCHANGED)
grayscale = cv2.imread(image_name, flags=cv2.IMREAD_GRAYSCALE)
color = cv2.imread(image_name, flags=cv2.IMREAD_COLOR) 


# TODO resize image with 'resize'
resized = cv2.resize(color, (100, 100))

# TODO rotate image (but keep it rectangular) with 'rotate'
rotated = cv2.rotate(resized, ROTATE_90_CLOCKWISE)

# TODO save image with 'imwrite'
cv2.imwrite('./01edited.jpg', rotated)

# TODO show the image with 'imshow'
cv2.imshow('IMAGE', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
