From Vector Import Vector

class Body(Vector):
    def __init__(self , mass , displacement=Vector() , velocity = Vector() , acceleration = Vector):
        self.mass = mass
        self.displacement = displacement
        self.velocity = velocity
        self.acceleration = acceleration
        self.total_displacement = []
        self.total_velocity = []
        self.total_acceleration = []
    def update_Acceleration(self,other):
        G = 6.674e11
        displacement = Vector()
        self.acceleration = ( G * other.mass) * (1.0/Vector.mag(other.displacement - self.displacement)**3) * (other.displacement - self.displacement) 
        return self.acceleration
        
    def update_velocity(self,t):
        self.velocity = self.velocity + (self.acceleration * t)
        return self.velocity
    
    def update_displacement(self,t):
        self.displacement = self.position + (self.velocity * t )
        return self.displacement
        
    def update_total_displacement(self,t):
        self.total_displacement.append(Body.update_displacement(self,t))
        return self.total_displacement
    
    def update_total_velocity(self,t):
        self.total_velocity.append(Body.update_velocity(self,t))
        return self.total_velocity
    
    def update_total_acceleration(self,other):
        self.total_acceleration.append(Body.update_Acceleration(self,other))
        return self.total_acceleration

def integration(body1, body2):
        #define some time stamp
        for #time stamp loop here#
        
        for t in tpoints:
            Body.append()
            k1 = h*f(r, t)
            k2 = h*f(r + 0.5*k1,t+0.5*h)
            k3 = h*f(r + 0.5*k2,t+0.5*h)
            k4 = h*f(r + k3,t+h)
            r += (k1+2*k2+2*k3+k4)/6.0
        
def calculate(Bodies):
    i=0
    while(i<len(Bodies)):
        j=0
        while(j<len(Bodies)):
            if i!=j:
                integration(Bodies[i], Bodies[j])
            j+=1
        i+=1
                
                
    
    for every body B in Bodies:

        for everyother body B'' in Bodies:
            integration(B, B'')
