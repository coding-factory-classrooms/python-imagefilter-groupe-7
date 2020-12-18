import cv2
import logger

def filter_grayscale(image):
    """

    :param image: L'image sur laquelle on va appliquer le filtre
    :return: L'image avec le filtre appliqué
    """
    #  Applique un filtre Noir&Blanc sur l'image
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    logger.log_in_file('  Applying a grayscale filter...')
    # retourne l'image avec le filtre
    return image_gray
