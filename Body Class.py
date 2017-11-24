# -*- coding: utf-8 -*-
"""
Created on Tue May 23 23:48:34 2017

@author: Ahmed Shalabi
"""
From Vector Import Vector

"""
Class object to store a particle's at any given timestep during the simulation.
"""
class Body(Vector):
    def __init__(self , mass , displacement=Vector() , velocity = Vector() , acceleration = Vector):
        self.mass = mass
        self.displacement = displacement
        self.velocity = velocity
        self.acceleration = acceleration
        self.total_displacement = []
        self.total_velocity = []
        self.total_acceleration = []
        typecheck([mass, displacement, acceleration], [float, float, float])
		try:
			assert mass > 0.0
		except:
			raise ValueError("mass must be greater than zero!")

    def update_Acceleration(self,other):
        G = 6.674e11
        displacement = Vector()
        self.acceleration = ( G * other.mass) * (1.0/Vector.mag(other.displacement - self.displacement)**3) * (other.displacement - self.displacement) 
        return self.acceleration
        
    def update_velocity(self,t):
        velocity = Vector()
        self.velocity = self.velocity + (self.acceleration * t) # t is the timestep
        return self.velocity
    
    def update_displacement(self,t):
        acceleration = Vector()
        self.displacement = self.position + (self.velocity * t )
        return self.displacement
        
    def copy(self):
        return (self.mass, self.displacement, self.velocity)
    
    def update_total_displacement(self,t):
        self.total_displacement.append(Body.update_displacement(self,t))
        return self.total_displacement
    
    def update_total_velocity(self,t):
        self.total_velocity.append(Body.update_velocity(self,t))
        return self.total_velocity
    
    def update_total_acceleration(self,other):
        self.total_acceleration.append(Body.update_Acceleration(self,other))
        return self.total_acceleration
    
