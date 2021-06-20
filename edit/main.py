import cv2

image = cv2.imread('pic/1.jpg')
image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# ========== Pic1 ============
# print(image.shape)
rows = image.shape[0]
columns = image.shape[1]

for i in range(rows):
    for j in range(columns):
        image[i, j] = 255 - image[i, j]

# ========== Pic2 ============

# print(image.shape)
# rows = image.shape[0]
# columns = image.shape[1]
#
# for i in range(rows):
#     for j in range(columns):
#         image[i, j] = 255 - image[i, j]

cv2.imshow('Edit', image)
# cv2.imwrite('README1.jpg', image)
cv2.waitKey()
