from Vector import Vector
from N Body import N Body
"""
     
    for body in Bodies:
        for body in Bodies:
            integration(self,other)
            update_displacement(self)
            update_total_displacement(self)"""

def integration(body1, body2):
        #define some time step
        for i in range(self.N):
            
			p = self.particles[i]
			displacement.append(p)
			acceleration = []
			for j in range(i) + range(i+1, self.N):
				p2 = self.particles[j]
				# Gravitational forces
				update_total_acceleration()

        for t in tpoints:
            Body.append()
            k1 = h*f(r, t)
            k2 = h*f(r + 0.5*k1,t+0.5*h)
            k3 = h*f(r + 0.5*k2,t+0.5*h)
            k4 = h*f(r + k3,t+h)
            r += (k1+2*k2+2*k3+k4)/6.0

def Gravitational_effect(self, p1, p2):
    	dx = p1.x - p2.x
    	dy = p1.y - p2.y
    	r = p1.dist(p2)
    	f = - p1.m * p2.m / (r**2 + self.a**2)
    	return [f*dx, f*dy]
    
def take_step(self):
	for i in range(self.N):
		update_total_acceleration(self).updates

  def calculate(Bodies):
    i=0
    while(i<len(Bodies)):
        j=0
        while(j<len(Bodies)):
            if i!=j:
                integration(Bodies[i], Bodies[j])
            j+=1
        i+=1
