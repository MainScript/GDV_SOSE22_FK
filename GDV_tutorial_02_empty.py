import cv2

image_name = './Cat03.jpg'
# TODO load images in grey and color
grayscale = cv2.imread(image_name, flags=cv2.IMREAD_GRAYSCALE)
color = cv2.imread(image_name, flags=cv2.IMREAD_COLOR) 

# TODO do some print out about the loaded data
print(color)

# TODO Continue with the color image or the grayscale image


# TODO Extract the size or resolution of the image
size = (len(grayscale), len(grayscale[0]))
print(size)

# TODO resize image
resized = cv2.resize(grayscale, (100,100))

# TODO print first row
print(resized[0])

# TODO print first column
print(grayscale[:,0])

# TODO set an area of the image to black
for x in range(30):
    for y in range(30):
        resized[x+30][y+50] = 0

# TODO find all used colors in the image
colors = []
for x in range(len(resized)):
    for y in range(len(resized[0])):
        if not resized[x][y] in colors:
            colors.append(resized[x][y])

print(colors)

# TODO copy one part of an image into another one
resized[0:20, 0:20] = resized[30:50, 30:50]

# TODO save image
cv2.imwrite('./02edited.jpg', resized)

# TODO show the image
cv2.imshow('IMAGE', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

# TODO show the original image (copy demo)
cv2.imshow('IMAGE', grayscale)
cv2.waitKey(0)
cv2.destroyAllWindows()