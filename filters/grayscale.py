import cv2

def filter_grayscale(image):
    #  Applique un filtre Noir&Blanc sur l'image
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # retourne l'image avec le filtre
    return image_gray