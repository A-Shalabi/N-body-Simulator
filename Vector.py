# -*- coding: utf-8 -*-
"""
@author: Ahmed Shalabi
"""

from math import sqrt , acos , cos

class Vector(object):
    def __init__(self, Input = []):
        self.data = Input
        
    
    def __repr__(self):
        return (self.data)
    
    def __add__(self,other):
        data = []
        i = 0
        while (i < len(self.data)):
            data.append(self.data[i] + other.data[i])
            i += 1
        return data
        
    def __sub__(self,other):
        data = []
        i=0
        while(i<len(self.data)):
            data.append(self.data[i] - other.data[i])
            i += 1
        return data
    
    def __mul__(self, v):
        data =[]
        i=0
        while(i<len(self.data)):
            data.append( v * self.data[i] )
            i += 1
        return data
    
    def dot(self,other):
        dot_product = 0
        i=0
        while(i<len(self.data)):
            dot_product += (self.data[i] * other.data[i])
            i+=1
        return dot_product
    
    def norm(self):
        dot_product = self.dot(self)
        norm = sqrt(dot_product)
        return norm
    
    def unit(self):
        norm = self.norm()
        unit_vec = self*(1.0 / norm )
        return unit_vec
    
    def angle(self,other):
        dot_product = self.dot(other)
        print(dot_product)
        norm_A = self.norm()
        norm_B = other.norm()
        temp = dot_product/(norm_A*norm_B)
        if temp>1.0:
            temp = 1.0
            
        theta = acos(temp)
        return theta
        
