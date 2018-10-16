import numpy as np
import cv2

img = cv2.imread('C:/Users/natha/PycharmProjects/plateGuard/test_plates/isfierce.png')
W = img.shape[1]
H = img.shape[0]

cv2.imshow('image',img)
k = cv2.waitKey(0)

for x in range(0, W):
    for y in range(0, H):
        # img[y,x] = (500,500,500)
        img.itemset((y, x, 0), 0)
        img.itemset((y, x, 1), 0)
        img.itemset((y, x, 2), 0)
cv2.imshow('image',img)
k = cv2.waitKey(0)
