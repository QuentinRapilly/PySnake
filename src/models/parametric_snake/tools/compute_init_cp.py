import numpy as np 
from math import cos, pi

def c(M : int, n : np.array):
    alpha = 2*(1 - cos(2*pi/M))/(cos(pi/M)-cos(3*pi/M))
    return alpha*np.cos(2*pi*n/M)

def s(M : int, n : np.array):
    alpha = 2*(1 - cos(2*pi/M))/(cos(pi/M)-cos(3*pi/M))
    return alpha*np.sin(2*pi*n/M)

def create_init_control_points(M1 : int, M2 : int, verbose : bool = False):
    k = np.arange(0, M1, 1)
    l = np.arange(-1, M2+2, 1)

    # TODO : arranger pour avoir chaque tableau en 2D
    x = np.expand_dims(np.expand_dims(c(M1,k),0)*np.expand_dims(s(2*M2,l),1),0)
    y = np.expand_dims(np.expand_dims(s(M1,k),0)*np.expand_dims(s(2*M2,l),1),0)
    z = np.expand_dims(np.repeat(np.expand_dims(c(2*M2,l),1),len(k), axis = 1),0)

    if verbose :
        print("Shapes of : \n-x : {},\n-y : {},\n-z : {}".format(x.shape, y.shape, z.shape))

    control_points = np.swapaxes(np.vstack((x,y,z)),0,2)

    if verbose : 
        print("Shape of control points : {}".format(control_points.shape))

    return control_points
