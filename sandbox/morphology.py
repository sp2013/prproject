import cv2
import numpy as np

def erode(image):

    img = cv2.imread(image)
    if img is None:
        print("Can not open or find the image.")

    kernel = np.ones((9,9), np.uint8)
    erode = cv2.erode(img, kernel, iterations=1)

    cv2.imshow("Input", img)
    cv2.imshow("Erode", erode)

    cv2.waitKey();
    cv2.destroyAllWindows()
    return