import sys
sys.path.append('../sandbox') # required to import package sandbox setting relative path.
from sandbox import *

import cv2

import opencvops as cvobj
import numpyops as npops
from sampleClass import MyPythonClass
import basicimaging as img
import mouseinterface as mouse
import morphology as morph
import connectedcomponents as cc
import logicaloperations as lp
import colorspaces as cs
import filters as filter
import histograms as hist

# two different ways of importing 'simplefunctions'
from simplefunctions import *
import simplefunctions as obj

# importing ML class
from machinelearning import ML

appleimage = '/home/priyal/Pictures/test/apples.jpg' # 224 x 224
morphimage0 = '/home/priyal/Pictures/test/morph0.png' # 500 x 500
morphimage1 = '/home/priyal/Pictures/test/morph1.png' # 850 x 760
morphimage2 = '/home/priyal/Pictures/test/morph2.png' # 850 x 760
juggballs = '/home/priyal/Pictures/test/balls.jpg'   # 800 x 600
grayimg = '/home/priyal/Pictures/test/flower_gray.jpg'   # 800 x 600
flower = '/home/priyal/Pictures/test/flower.jpg'   # 800 x 600
histo0 = '/home/priyal/Pictures/test/histo_0.bmp'   # 800 x 600


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

def testbasicimaging():
    img.cropresize(appleimage)
    img.rotateimage(appleimage, 45)
    img.drawshapes(appleimage)
    return

def testmouseinterface():
    mouse.launchcircledraw()
    return

def testmorphology():
    morph.erode(morphimage0)
    morph.dilate(morphimage0)
    morph.open(morphimage1)
    morph.close(morphimage2)
    return

def testconnectedcomponents():
    #cc.ccanalysis(morphimage0)
    cc.ccanalysiswithstats(morphimage0)
    return

def testlogicaloperations():
    # lp.logicaloperations()
    # lp.applymask(juggballs)
    lp.splitnmerge(juggballs)
    return

def testcolorspaces():
    cs.colorspaces(juggballs)
    return

def testfilters():
    filter.BilateralBlur(grayimg)
    # filter.MedianBlur(grayimg)
    # filter.GaussianSmooth(grayimg)
    # filter.averaging(appleimage)
    return

def testhistograms():
    hist.histoequalize(grayimg)
    # hist.grayhistogram(histo0 )
    # hist.colorhistogram(appleimage)
    return




