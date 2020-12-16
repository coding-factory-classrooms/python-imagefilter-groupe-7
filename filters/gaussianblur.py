import cv2

def filter_blur(image):
    # Applique un filtre de flou
    image_blur = cv2.GaussianBlur(image, (5, 5), 5)
    # retourne l'image avec le filtre
    return image_blur

