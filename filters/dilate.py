import cv2
import numpy as np
import logger

def filter_dilate(image):
    # Applique un filtre Dilatation
    kernel = np.ones((5, 5), np.uint8)
    image_dilate = cv2.dilate(image,kernel, iterations=2)
    logger.log_in_file('  Applying a dilate filter...')
    # retourne l'image avec le filtre
    return image_dilate
