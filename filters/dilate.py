import cv2
import numpy as np
import logger

def filter_dilate(image, value):
    """

    :param image: L'image sur laquelle on va appliquer le filtre
    :param value: Le nombre de fois qu'on va appliquer le filtre sur l'image
    :return: L'image avec le filtre appliqué
    """
    # Applique un filtre Dilatation
    kernel = np.ones((5, 5), np.uint8)
    image_dilate = cv2.dilate(image,kernel, iterations=value)
    logger.log_in_file('  Applying a dilate filter...')
    # retourne l'image avec le filtre
    return image_dilate
