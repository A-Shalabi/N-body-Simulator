# -*- coding: utf-8 -*-
"""
Created on Mon May 22 00:00:57 2017

@author: Ahmed Shalabi
"""

from math import sqrt , acos 

class Vector(object):
    def __init__(self, Input = []):
        self.data = Input
        
    
    def __repr__(self):
        return (self.data)
    
    def __add__(self,other):
        data = []
        for i in len(range(self.data)):
            data.append(self.data[i] + other.data[i])
        return data
        
    def __subt__(self,other):
        data = []
        for i in len(range(self.data)):
            data.append(self.data[i] - other.data)
        return data
    
    def __mult__(self, v ):
        data =[]
        for i in len(range(self.data)):
            data.append( v * self.data[i] )
        return data
    
    def __dot__(self,other):
        dot_product = 0
        for i in len(range(self.data)):
            dot_product += (self.data[i] * self.data[i])
        return dot_product
    
    def __norm__(self):
        dot_product = Vector.dot (self,self)
        norm = sqrt(dot_product)
        return norm
    
    def __unit__(self):
        norm = Vector.norm(self)
        unit_vec = Vector.__mult__(self , 1.0 / norm )
        return unit_vec
    
    def __angle__(self,other):
        dot_product = Vector.dot(self,other)
        norm_A = Vector.norm(self)
        norm_B = Vector.norm(other)
        theta = acos(dot_product/norm_A*norm_B)
        return theta
        
V1 = Vector([0,0,0])
V2 = Vector([1,1,1])
print(V1+V2)
        
        
        