from fn1 import *
import fn1 as obj
from sampleClass import *
from machinelearning import *
import opencvops as cvobj
import skimageops as sk


if __name__ == '__main__':

    print('Entering main function')

    print(greetings())

    obj.fun1() # using obj for calling function.
    fun1();  # directly calling the function.

    objML = ML() # instantiate ML class
    objML.train()

    imageName = '/home/priyal/Pictures/test/apples.jpg'

    sk.displayimage(imageName)
    cvobj.displaynumpyarray(imageName)
    cvobj.addsquareatcenter(imageName, (0, 0, 0))
    cvobj.addghorzstripes(imageName, (255, 0, 0)) # order is bgr
    cvobj.addgvertstripes(imageName, (0, 0, 255))  # order is bgr
    cvobj.createnparrays()




