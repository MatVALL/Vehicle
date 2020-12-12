import numpy as np
class Map():
    def __init__(self,size,d1,d2):
        self.size=size
        self.obstacles=np.array(size)
        self.d1 = d1
        self.d2 = d2
    def positionIsValid(self,pos):
        i=pos[0]
        j=pos[1]
        I=np.array([1,i,i**2,i**3])
        j1=self.d1@I
        j2=self.d2@I
        if(j1>j and j>j2):
            return True
        return False
    def positionIsGoal(self,pos):
        return self.positionIsValid(pos) and pos[0]>=550
    #rotate it ?
    def getNeighbourhood(self,pos,angle):
        n=np.ones((16,16))
        for i in range(-n.shape[0]//2,n.shape[0]//2):
            for j in range(-n.shape[1]//2,n.shape[1]//2):
                #https://academo.org/demos/rotation-about-point/
                a = np.radians(angle%360)
                i_rotated = int(i*np.cos(a))-int(j*np.sin(a)) #x*cos0 - y*sin0
                j_rotated = int(i*np.sin(a))+int(j*np.cos(a)) #x*sin0 + y*cos0
                i_centered = pos[0]+i_rotated*12
                j_centered = pos[1]+j_rotated*12

                if self.positionIsValid((i_centered,j_centered)):
                    n[i+n.shape[0]//2][j+n.shape[1]//2]=0
                else:
                    n[i+n.shape[0]//2][j+n.shape[1]//2]=1
        return n
