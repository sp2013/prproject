import numpy as np
import cv2

def logicaloperations():

    # create numpy image with white square
    rectangle = np.zeros((400, 400), dtype="uint8")
    cv2.rectangle(rectangle, (50, 50), (350, 350), 255, -1)
    cv2.imshow("Rectangle", rectangle)

    # create numpy image with white circle.
    circle = np.zeros((400, 400), dtype="uint8")
    cv2.circle(circle, (200, 200), 175, 255, -1)
    cv2.imshow("Circle", circle)
    cv2.waitKey()
    cv2.destroyAllWindows()

    # bitwise logical AND operation
    bitwiseAnd = cv2.bitwise_and(rectangle, circle)
    cv2.imshow("AND", bitwiseAnd)
    cv2.waitKey(0)

    # bitwise logical OR operation
    bitwiseOr = cv2.bitwise_or(rectangle, circle)
    cv2.imshow("OR", bitwiseOr)
    cv2.waitKey(0)

    # bitwise logical XOR operation
    bitwiseXor = cv2.bitwise_xor(rectangle, circle)
    cv2.imshow("XOR", bitwiseXor)
    cv2.waitKey(0)

    # bitwise logical NOT operation
    bitwiseNot = cv2.bitwise_not(circle)
    cv2.imshow("NOT", bitwiseNot)
    cv2.waitKey(0)

    cv2.destroyAllWindows()
    return


def applymask(image):

    input = cv2.imread(image)
    cv2.imshow("Input Image", input)
    cv2.waitKey()

    print("image shape: {}".format(input.shape[:2])) # display image dimensions.

    width = input.shape[0]
    height = input.shape[1]
    mask = np.zeros(input.shape[:2], dtype = "uint8")
    (cX, cY) = (input.shape[1], input.shape[0]) # number of rows at index 0, cols at index 1
    cv2.rectangle(mask, (200, 200), (cX-200, cY-200), 255, -1)
    cv2.imshow("Mask", mask)
    cv2.waitKey()

    masked = cv2.bitwise_and(input, input, mask=mask)
    cv2.imshow("Mask Applied to Image", masked)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return


'''
    split input image in to R, G and B channels...merge it back.
'''
def splitnmerge(image):

    input = cv2.imread(image)
    (B, G, R) = cv2.split(input)
    cv2.imshow("Red", R)
    cv2.imshow("Green", G)
    cv2.imshow("Blue", B)
    cv2.waitKey(0)

    merged = cv2.merge([B, G, R])
    cv2.imshow("Merged", merged)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    zeros = np.zeros(input.shape[:2], dtype="uint8")
    cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
    cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
    cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
    cv2.waitKey(0)

    return

