import cv2
import logger

def filter_blur(image, value):
    """

    :param image: L'image sur laquelle on va appliquer le filtre
    :param value: Intensité du filtre
    :return: L'image avec le filtre appliqué
    """

    # Applique un filtre de flou
    image_blur = cv2.GaussianBlur(image, (value, value), 9)
    logger.log_in_file('  Applying a blur filter...')
    # retourne l'image avec le filtre
    return image_blur

