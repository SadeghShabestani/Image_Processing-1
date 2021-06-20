import cv2
from numpy.ma import clump_masked

image = cv2.imread('pic/3.jpg')
image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
image = cv2.resize(image, (700, 700))

# print(image.shape)
rows = image.shape[0]
columns = image.shape[1]
rotation = cv2.getRotationMatrix2D((rows / 2, columns / 2), 180, 0.5)
# print(rotation)
rotation_image = cv2.warpAffine(image, rotation, (rows, columns))
image = cv2.imshow('Happy', rotation_image)
# cv2.imwrite('Happy.jpg', rotation_image)
cv2.waitKey()
