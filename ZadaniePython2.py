#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 13:48:55 2018

@author: Gosia
"""

##### ZADANIE 1
import moj_folder.moje_funkcje as fn

fn.napisik("Pozdro Jaco")


##### ZADANIE 2

def double(x):
    if isinstance(x, (int, float))==True:
        double_x=x*2
    else: 
        double_x=[i*2 for i in x]
        x=x*2
    return x, double_x


print(double(5))
print(double(5.))
print(double([1,2]))

x = 3.
print(double(x) == (3., 6.))
print(x == 3.)

z = [3]
print(double(z) == ([3, 3], [6]))
print(z == [3])

w = [1, 2, 3]
print(double(w) == ([1, 2, 3, 1, 2, 3], [2, 4, 6]))
print(w == [1, 2, 3])