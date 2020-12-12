import numpy as np

class Vehicle():
    def __init__(self,x,y,angle):
        self.x,self.y=x,y#position en X et en Y
        self.angle=angle
        self.inertie=(0,0)
        self.acceleration=0
    def move(self):
        self.x += self.inertie[0]
        self.y += self.inertie[1]
        self.updateInertie()
    def updateInertie(self):
        #les x deviennent les x + leurs inerties soumises aux frottements
        inertie_x =  self.acceleration*np.sin(np.radians(self.angle))+0.8*self.inertie[0]
        inertie_y =  self.acceleration*np.cos(np.radians(self.angle))+0.8*self.inertie[1]
        self.inertie=(inertie_x,inertie_y)
    def getSpeed(self):
        return np.linalg.norm(self.inertie)
    def rotate(self,angle_difference):
        self.angle += angle_difference
