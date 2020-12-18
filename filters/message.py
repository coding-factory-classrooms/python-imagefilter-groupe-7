import cv2
import logger


def filter_message(image, msg):
    '''
    :param image: L'image sur laquelle on va appliquer le filtre
    :param msg: Le message récupéré et ecris sur l'image
    :return: L'image avec le filtre appliqué
    '''

    image_message = cv2.putText(image, msg, (10, 150), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255))
    logger.log_in_file('  Applying a blur filter...')
    return image_message