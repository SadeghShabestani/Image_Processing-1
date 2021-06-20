import cv2

image = cv2.imread('pic/4.jpg')
image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# print(image.shape)

rows = image.shape[0]
columns = image.shape[1]

for i in range(rows):
    for j in range(columns):
        if image[i, j] < 70:
            image[i, j] = 0
        elif image[i, j] > 70:
            image[i, j] = 255

cv2.imshow('Input Image', image)
# cv2.imwrite('README.jpg', image)
cv2.waitKey()
