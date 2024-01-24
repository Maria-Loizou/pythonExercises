#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 22:32:03 2021

@author: MariaLoizou
"""
#a
e2f = { 'dog':'chien', 'cat':'chat', 'walrus':'morse'}

#b
print (e2f['walrus'])

#c
tup = e2f.items()
f2e = dict((y, x) for x, y in tup)

#d
print (f2e['chien'])

#e
for x in e2f.keys():
      print(x)