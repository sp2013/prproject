import numpy as np
import cv2

def averaging(imgpath):

    image = cv2.imread(imgpath)
    blurred = np.hstack([
        cv2.blur(image, (3, 3)),
        cv2.blur(image, (5, 5)),
        cv2.blur(image, (15, 15))])
    cv2.imshow("Averaged", blurred)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return