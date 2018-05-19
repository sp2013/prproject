import cv2
import math

'''
This program shows how highgui enables us to take mouse inputs. In this
code we use mouse input to draw a circle on an image. The mouse is dragged 
from the center to one of the points on the circumference. ‘c’ can be 
pressed to remove the drawn circles. '''

# Lists to store the points
center = []
ptoncircle = []

'''
drawcircle is a call back function that is called when there is a mouse event like 
left click (EVENT_LBUTTONDOWN ). This function captures the click point is (x, y) from
the named window to which the call back function is attached. The 
function records the points of the circle’s center and a point on the 
circumference, so that we can compute radius of circle to be drawn.
'''

source = cv2.imread('/home/priyal/Pictures/test/tomatoes.jpg')

def drawcircle(action, x, y, flags, userdata):
    # Referencing global variables
    global center, ptoncircle
    # Action to be taken when left mouse button is pressed
    if action == cv2.EVENT_LBUTTONDOWN:
        center = [(x, y)]
        # Mark the center
        cv2.circle(source, center[0], 1, (255, 255, 0), 2, cv2.LINE_AA);

    # Action to be taken when left mouse button is released
    elif action == cv2.EVENT_LBUTTONUP:
        ptoncircle = [(x, y)]
        # Calculate radius of the circle
        radius = math.sqrt(math.pow(center[0][0] - ptoncircle[0][0], 2)
                           + math.pow(center[0][1] - ptoncircle[0][1], 2))
        # Draw the circle
        cv2.circle(source, center[0], int(radius), (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow("Draw Circle", source)


def launchcircledraw():

        global source
        srccopy = source.copy() # copy of image used to overwrite circle drawing
        cv2.namedWindow("Draw Circle")

        # drawcircle function called when mouse events occur
        cv2.setMouseCallback("Draw Circle", drawcircle)
        k = 0

        #loop until escape character is pressed
        while k != 27:

            cv2.imshow("Draw Circle", source) # display image,
            cv2.putText(source, "Choose center and drag, Press ESC to exit and x to clear",
                        (10, 30), cv2.FONT_ITALIC,
                        0.7, (255, 255, 255), 2);
            k = cv2.waitKey(20) & 0xFF

            if k == 120:
                source = srccopy.copy()

        cv2.destroyAllWindows()