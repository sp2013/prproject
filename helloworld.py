from fn1 import *
import fn1 as obj
from sampleClass import *
from machineLearning import *

if __name__ == '__main__':

    print('Entering main function')

    obj.fun1() # using obj for calling function.

    fun1();  # directly calling the function.

    #displayImage('/home/priyal/Pictures/app1.png')
    displayImage('/media/priyal/427E3C177E3C0667/DG_images/medc.jpg') #here media is partitioned drive.

    obj = ML()
    obj.train()


