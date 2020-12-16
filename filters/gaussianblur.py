import cv2

def blur():
    try:
        image = cv2.imread('data/img/imageTest.jpeg')
        newImg = cv2.GaussianBlur(image, (5, 5), 5)
        cv2.imwrite('data/output/newImage.jpeg', newImg)
    except cv2.error as e:
        print(e)