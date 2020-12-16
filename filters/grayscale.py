import cv2

def grayscale():

    image = cv2.imread('data/img/imageTest.jpeg')
    newImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('data/output/newImage.jpeg', newImg)