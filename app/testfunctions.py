import sys
sys.path.append('../sandbox')

from sandbox import *

import opencvops as cvobj
import numpyops as npops
from sampleClass import MyPythonClass

# two different ways of importing 'simplefunctions'
from simplefunctions import *
import simplefunctions as obj

# importing ML class
from machinelearning import ML

appleimage = '/home/priyal/Pictures/test/apples.jpg'

def testclass():
    classobj = MyPythonClass()
    return

def testopencvops():
    cvobj.displaynumpyarray(appleimage)
    cvobj.addsquareatcenter(appleimage, (0, 0, 0))
    cvobj.addghorzstripes(appleimage, (255, 0, 0)) # order is bgr
    cvobj.addgvertstripes(appleimage, (0, 0, 255))  # order is bgr
    cvobj.createnparrays()
    cvobj.readwritedisplay()
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
    npops.createsomemorematrices()
    npops.datatypesconversion()
    return