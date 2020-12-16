import cv2

def blur():
    image = cv2.imread('data/img/imageTest.jpeg')
    newImg = cv2.GaussianBlur(image, (5, 5), 5)
    cv2.imwrite('data/output/newImage.jpeg', newImg)