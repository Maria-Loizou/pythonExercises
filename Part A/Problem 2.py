#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 15:34:29 2021

@author: MariaLoizou
"""

'''Define function '''

def intersect (L1, L2): 
    '''Initiate list '''
    intersection = []
    for elem1 in L1:
        for elem2 in L2:
            if elem1 == elem2 and elem1 not in intersection:
                intersection.append(elem1)
    return intersection     

print(intersect(L1,L2))

'''
Function iterates through the tow lists. 

It uses the membership operators is and is not to check if elem1 of L1 is the 
same as elem1 of L2 or if it is already in the list. 

If the elements are the same and not already in the list the element is 
appended in the list. 

The function returns the intersection of the two lists. 

'''
