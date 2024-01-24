#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 09:16:56 2021

@author: MariaLoizou
"""


def pguess(coeficients,guess):
    polynom = 0
    power = (len(coeficients))-1
    for i in coeficients:
        value = i * guess ** power
        power -= 1 
        polynom += value
    return(polynom)



def derivPguess(coeficients,guess):
    derivPolynom = 0
    power = (len(coeficients))-1
    for i in coeficients: 
        value = (i * power) * (guess ** (power-1))
        power -= 1
        derivPolynom += value
    return (derivPolynom)



def NR_approximation (coeficients,guess):
    approx = guess - pguess(coeficients, guess)/derivPguess(coeficients, guess)
    return approx 



def NR_Root(coeficients, guess, epsilon):
    while pguess(coeficients,guess) >= epsilon:
        guess = NR_approximation(coeficients,guess)
    return guess

        

''''
The first functions uses a for loop to calculate the value of the polynomial 
based on the coefficients tuple. 

Similarly, the second function uses a for loop to calculates the value of the 
derivative of thepolynomial. 

A third function is created that uses the functions mentioned above to 
apply the Newton-Raphson method to the initial guess value. 

Finally, a function that uses a while loop is created which applies the 
Newton-Raphson approximation to the initial guess value  as long as the 
result of the polynomial is greater than the epsilon value. 
'''



        