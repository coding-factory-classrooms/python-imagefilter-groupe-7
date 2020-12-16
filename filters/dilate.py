import cv2
import numpy as np

def dilate():
    image = cv2.imread('data/img/imageTest.jpeg')
    kernel = np.ones((5, 5), np.uint8)
    dilate = cv2.dilate(image,kernel, iterations=15)
    cv2.imwrite('data/output/newImage.jpeg', dilate)