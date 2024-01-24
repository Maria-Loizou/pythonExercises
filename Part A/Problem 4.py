#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 13:18:17 2022

@author: MariaLoizou
"""
import random
import numpy as np 
from numba import jit 

totalNumbers = 10000000

#Part I - Iterative Loop 

"""Creates a function that generates  a given number (n) of random values 
   between 0 and 1 and then finds their average. 
"""
def average_py(n):
    randomNumbers = 0
    
    for i in range(n):
        x = random.uniform(0,1)
        randomNumbers += x
        
    
    average = randomNumbers/n
    return average 

%time print('Part I =',average_py(totalNumbers))

#Part II - List comprehension 

"""
Use list comprehenion to create a list that contains a given number of random values 
between 0 and 1 and then use the function sum to find their average. 
"""

%time average = sum([random.uniform(0,1) for i in range(totalNumbers)])/totalNumbers
print('Part II =',average)


#Part III - NumPy Library 

"""
Use the numpy library to create a numpy array containing a given number of random values 
between 0 and 1 and then use the mean method to find their average.  
"""


def average_np(n):
    randomNumbers = np.random.uniform(0,1,n)
    return randomNumbers.mean()
        
%time print('Part III =', average_np(totalNumbers))
  



#Part IV - Numba 

""""
Use numba to optimise the average_nb function 
"""


average_nb = jit(average_py)

%time print('Part IVa =', average_nb(totalNumbers))
%time print('Part IVb =',average_nb(totalNumbers))


'''

(a) What is the order of the above in execution times starting from the slowest?

II  - List comprehension
I   - Iterative Loop 
III - NumPy Library 
IV  - Numba 

(b) Which from (i) to (iv) has the least execution time.

IV - Numba 

'''





