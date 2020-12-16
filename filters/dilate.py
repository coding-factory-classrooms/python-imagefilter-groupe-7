import cv2
import numpy as np

def dilate(iteration):
    try:
        image = cv2.imread('data/img/test.txt')
        kernel = np.ones((5, 5), np.uint8)
        dilate = cv2.dilate(image,kernel, iterations=iteration)
        cv2.imwrite('data/output/newImage.jpeg', dilate)
    except cv2.error as e:
        print(e)