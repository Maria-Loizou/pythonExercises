#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 16:06:20 2022

@author: MariaLoizou
"""
import matplotlib.pyplot as plt 
import numpy as np


#Bisection Function (arguments: function, lower bound, upper bound, tolerance)
def Bisection(f,a,b,tol):
    xl=a
    xr=b
    while xr-xl>tol:
        c = (xl+xr)/2
        prod = f(xl)*f(c)
        
        if prod>tol:
            xl=c
        elif prod<tol:
                xr=c
    
    return c

# Part A 
                
#Equation to solve
def f1(x):
    return x**2 + 5*x + 2 

#Plot the function to get an appropriate range for the bisection iteration 
x = np.linspace(-10,10,1000)
plt.plot(x,f1(x))
plt.ylim(-10,20)
plt.grid()
plt.show()

#Solve for approximation of the first root 
print ('Part A 1st root =', Bisection(f1, -5,-2.5 , 0.000001))

#Solve for the approximation of the second root 
print ('Part A 2nd root =', Bisection(f1, -2.5,0, 0.000001))


# Part B 

#Equation to solve
def f2(x):
    return (x**3)+2*(x**2)-(6*x)+2

#Plot the function to get an appropriate range for the bisection iteration 
x = np.linspace(-10,10,100)
plt.plot(x,f2(x))
plt.ylim(-10,20)
plt.grid()
plt.show()

#Solve for approximation of the first root 
print ('Part B 1st root =', Bisection(f2, -5, 0, 0.000001))

#Solve for the approximation of the second root 
print ('Part B 2nd root =', Bisection(f2, 0,0.5, 0.000001))

#Solve for approximation of the third root 
print ('Part B 3rd root =', Bisection(f2, 0.5, 5 , 0.000001))











