import cv2
import numpy as np
import logger

def filter_dilate(image, value):
    # Applique un filtre Dilatation
    kernel = np.ones((5, 5), np.uint8)
    image_dilate = cv2.dilate(image,kernel, iterations=value)
    logger.log_in_file('  Applying a dilate filter...')
    # retourne l'image avec le filtre
    return image_dilate
