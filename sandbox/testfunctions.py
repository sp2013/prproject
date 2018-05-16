from simplefunctions import *
import simplefunctions as obj
from sampleClass import *
from machinelearning import *
import opencvops as cvobj
import numpyops as npops

appleimage = '/home/priyal/Pictures/test/apples.jpg'


def testopencvops():
    cvobj.displaynumpyarray(appleimage)
    cvobj.addsquareatcenter(appleimage, (0, 0, 0))
    cvobj.addghorzstripes(appleimage, (255, 0, 0)) # order is bgr
    cvobj.addgvertstripes(appleimage, (0, 0, 255))  # order is bgr
    cvobj.createnparrays()
    return


def testmachinelearning():
    objML = ML() # instantiate ML class
    objML.train()
    return


def testsimplefunctions():
    print(greetings())
    obj.fun1() # using obj for calling function.
    fun1();  # directly calling the function.
    return


def testnumpyops():
    npops.createarrays()
    npops.displayattributes()
    return