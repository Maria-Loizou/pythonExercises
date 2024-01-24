#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 21:07:16 2021

@author: MariaLoizou
"""



import numpy as np 

randomVar = 100000
radius = 0.5
totalInCircle = 0

for i in range(randomVar):
    x = np.random.uniform(0,1)
    y = np.random.uniform(0,1)

    dx = (radius-x)**2
    dy = (radius-y)**2
    dSquared = np.sqrt(dy+dx)

    if dSquared <= radius:
        totalInCircle += 1

pi = (totalInCircle / randomVar)/(radius**2)
print (pi)


''''
A for loop is created that assigns a random value between 0 and 1 to x and y. 
These values act as x,y coordinates to generate random points within a 1x1  
square. 

To figure out if the random points that were generated lie within the are of 
the circle, the formula to find the distance between two points is used to 
figure out the distance between the point and the centre of the circle. If the 
distance is less than the radius it means that the point lies within the circle
and and the count of variable totalInCircle increases by one.

This is repeated 100000 times. 

The probability of the random point to lie in the circle  is calculated by 
dividing the variable totalInCircle by 100000 (total number of points generated)

Since according to the monte carlo simualation since the probability of a point 
falling in the area of the circle is equal to the area of the circle, 
then dividing the probability by the radio give pi. 
''' 