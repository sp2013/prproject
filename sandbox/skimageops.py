import numpy as np
from skimage import io
from matplotlib import pyplot as plt


def displayimage(image):
    io.imshow(image)
    plt.show(image)