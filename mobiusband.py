#! /usr/bin/env python
'''
plot a Mobiusband
'''
from numpy import *
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm

'''
x,y,z functions
FUNC_X = '(1 + v / 2 * cos(u/2)) * cos(u)' 
FUNC_Y = '(1 + v / 2 * cos(u/2)) * sin(u)' 
FUNC_Z = 'v / 2 * sin(u/2)' #v,u
0<= u <= 2pi, -1<= v <=1
'''
SAMPLE = 500  # number of sample

def func_x(v, u):
    answer = [((1. + v / 2. * cos(value_u/2.)) * cos(value_u)) for value_u in u]
    return array(answer)
    
def func_y(v, u):
    answer = [((1. + v / 2. * cos(value_u/2.)) * sin(value_u)) for value_u in u]
    return array(answer)

def func_z(v, u):
    answer = [(v / 2. * sin(value_u/2.)) for value_u in u]
    return array(answer)


def mobiusband():
    v = linspace(-1.0, 1.0, num=SAMPLE, endpoint=True)
    u = linspace(0, 2*pi, num=SAMPLE, endpoint=True)
    X = func_x(v, u)
    Y = func_y(v, u)
    Z = func_z(v, u)
    
    fig = plt.figure(dpi=150)
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X, Y, Z, cmap=cm.YlOrBr, alpha=0.9, linewidth=0)
    ax.set_zlim(-2., 2.) #longthen z_axes
    plt.axis('off')
    fig.savefig('mobiusband.png', transparent=True, dpi=600)
    
    plt.show()

      
        
if __name__ == '__main__':
    mobiusband()
