import cv2
import numpy as np

rows = 800
columns = 800
# ============ create white Board ============
image = np.ones((rows, columns)) * 255

for i in range(rows):
    for j in range(columns):
        if (i // 100) % 2 == 0:
            if (j // 100) % 2 == 1:
                image[i, j] = 0
        else:
            if (j // 100) % 2 == 0:
                image[i, j] = 0
cv2.imshow('Chess', image)
# cv2.imwrite('chess.jpg', image)
cv2.waitKey()
