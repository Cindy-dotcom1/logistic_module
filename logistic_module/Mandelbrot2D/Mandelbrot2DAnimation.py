from numba import jit 
import matplotlib.pyplot as plt
from Mandelbrot2D import Mandelbrot_2D
from memory_profiler import profile

Z_2 = Mandelbrot_2D(500, 500, 600, -1.7, 0.2, -0.95, 0.95)
Z_3 = Mandelbrot_2D(500, 500, 600, -1.5, 0, -0.75, 0.75)
Z_4 = Mandelbrot_2D(500, 500, 600, -1.5, -0.35, -0.57, 0.57)
Z_5 = Mandelbrot_2D(500, 500, 600, -1.44,-0.72, -0.4,0.4)
Z_6 = Mandelbrot_2D(500, 500, 600, -1.42, -0.98, -0.2, 0.2)
Z_7 = Mandelbrot_2D(500, 500, 600,  -1.42,-1.23,-0.1,0.09)
Z_8 = Mandelbrot_2D(500, 500, 600, -1.41886,-1.27142,-0.0961,0.08658)
Z_9 = Mandelbrot_2D(500, 500, 600, -1.41,-1.3366,-0.05,0.05)

@profile
def animate(i):
    """Animated zoom on the mandelbrot set
    :param i: the number of time the functions is to be used
    :type i: integer

    :return: An image with a zoom on the Mandelbrot set
    :rtype: object 
    """
    #The programm passes this function multiples times: it goes from i=0 to a value of i that we are going to chose in the document script.py. For each value of i, we print a different matrice. As i increases, the interval for min values and max values (for x and y) becomes smaller, visuallly it is like if we were zooming on the first picture (obtained by printing Z)
    if i == 0:
        im = plt.imshow(Z_2.Mandelbrotset)
    if i == 1:
        im = plt.imshow(Z_3.Mandelbrotset)
    if i == 2:
        im = plt.imshow(Z_4.Mandelbrotset)
    if i == 3:
        im = plt.imshow(Z_5.Mandelbrotset)
    if i == 4:
        im = plt.imshow(Z_6.Mandelbrotset)
    if i == 5:
        im = plt.imshow(Z_7.Mandelbrotset)
    if i == 6:
        im = plt.imshow(Z_8.Mandelbrotset)
    if i>=7:
        im=plt.imshow(Z_9.Mandelbrotset)
    return im,




