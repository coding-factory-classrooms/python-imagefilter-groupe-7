import cv2
import logger

def filter_grayscale(image):
    #  Applique un filtre Noir&Blanc sur l'image
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    logger.log_in_file('  Applying a grayscale filter...')
    # retourne l'image avec le filtre
    return image_gray
