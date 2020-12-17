import cv2
import logger

def filter_blur(image):

    # Applique un filtre de flou
    image_blur = cv2.GaussianBlur(image, (5, 5), 5)
    logger.log_in_file('  Applying a blur filter...')
    # retourne l'image avec le filtre
    return image_blur

