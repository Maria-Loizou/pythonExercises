#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 13:15:08 2021

@author: MariaLoizou
"""

listData=[
'prices',
'3',
'8',
'7',
{7:7, 6:6},
'21',
]


totalSum = 0

for i in listData: 
    try: totalSum += (int(i))
    except TypeError:
        print('Type error')
    except ValueError:
        print('Value error')
    except: 
        print ('other exception')
    
print(totalSum)

    
''''
The variable totalSum is initiated.

The for loop iterates through the array listData and and 
converts the elements into integers using the function int() and add them to 
the variable totalSum. 

The try-except method is used to capture errors for the elements that cannot 
be converted, it returns a statement based on the error type. 
It then proceeds to the next element. 
'''

    
