import sys
import cv2

args = sys.argv
for i in range(0, len(args)):
    arg = args[i]
    print(arg)
    if arg == '--color':
        image = cv2.imread('data/img/imageTest.jpeg')
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('data/output/newImage.jpeg', gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()