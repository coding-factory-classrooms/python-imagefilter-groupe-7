import cv2
import numpy as np

def filter_dilate(image):
    # Applique un filtre Dilatation
    kernel = np.ones((5, 5), np.uint8)
    image_dilate = cv2.dilate(image,kernel, iterations=2)
    # retourne l'image avec le filtre
    return image_dilate
