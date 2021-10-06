#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 12:41:31 2018

@author: harrymoo
"""

class point_:
    """Point_ holds x, y and z data"""
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z
        
    def __str__(self):
        return "{}, {}, {}".format(self.x, self.y, self.z)
    
    def __repr__(self):
        return self.__str__()