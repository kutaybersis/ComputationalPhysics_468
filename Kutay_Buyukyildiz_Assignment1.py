#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: bersiskutay
"""
from  sympy.solvers import solve
from sympy import Symbol
from sympy import Eq,solve_linear_system, Matrix
from numpy import linalg
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
from scipy import interpolate

time = (0,10,15,20,22.5,30)
velocity = (0 , 227.04 , 362.78 , 517.35 , 602.97 , 901.67)

xString = input('Time Value 1 : ')
x_x = int(xString)



#QUADRATIC INTERPOLATION

f = interpolate.interp1d(time, velocity, kind = 'quadratic')
print(f(x_x))

yString = input('Distance Between Time Value 2 :')
x_y = int(yString)

import scipy.integrate as integrate
result = integrate.quad(f,x_y,x_x)
result

print("Distance :", result ,"m")

xnew = np.arange(0,30, 0.1)
ynew = f(xnew)   
plt.plot(time, velocity, 'o', xnew, ynew, '-')
plt.show()

