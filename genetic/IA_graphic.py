import pygame
import vehicle, map, AI
import sys
import numpy as np
from game import *

def plotRotated(sprite,angle,center):
    sprite_rotated=pygame.transform.rotate(sprite,angle)
    new_rect = sprite_rotated.get_rect(center = sprite.get_rect(center=center).center)
    screen.blit(sprite_rotated, new_rect)

def plotMap(m,surface):
    for i in range(m.size[0]):
        I=np.array([1,i,i**2,i**3])
        j1=m.d1@I
        j2=m.d2@I
        COLOR=(255,255,255)
        if j1<m.size[1]:
            surface.fill(COLOR, ((i,j1), (1,1)))
        if j2<m.size[1]:
            surface.fill(COLOR, ((i,j2), (1,1)))

def plot(screen,v,angle_difference,map_s):
    plotMap(map_s,screen)
    pygame.font.init() # you have to call this at the start,
    myfont = pygame.font.SysFont('Arial', 10)
    textsurface = myfont.render(str(int(v.x))+","+str(int(v.y)), False, (255,255,255))
    screen.blit(textsurface,(0,120))
    plotRotated(sprite,v.angle+180,(v.x,v.y))

def plotState(surface,state,actions):
    global won, lost
    for i in range(state.shape[0]):
        for j in range(state.shape[1]):
            COLOR=(255,255,255)
            if state[i][j]==0:
                COLOR=(0,0,0)
            surface.fill(COLOR, ((5*i+30,5*j+30), (10,10)))

    pygame.font.init() # you have to call this at the start,
    myfont = pygame.font.SysFont('Arial', 10)

def race(model,m,graphic=False):
    v=vehicle.Vehicle(3,200,30)
    state = m.getNeighbourhood((v.x,v.y),v.angle)
    reward_sum=0
    for step in range(100):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver=True
        state = m.getNeighbourhood((v.x,v.y),v.angle)
        y=model.forward(np.array(state).flatten())
        action = actions[y.argmax()]
        apply_action(v,action)

        if(graphic):
            screen.fill(black)
            plotState(screen,state,actions)
            plot(screen,v,angle_difference,m)
            pygame.display.flip()

        reward= calculateReward(v,m)
        if step==9999:
            reward=-100
        reward_sum+= reward
        if gameIsOver(v,m):
            break;
    print(reward_sum)
    return reward_sum

if __name__=="__main__":
    sprite = pygame.image.load("cars.png")
    imagerect = sprite.get_rect()
    sprite=pygame.transform.smoothscale(sprite, (40,40))

    pygame.init()
    size = width, height = 600, 600
    black = 0, 0, 0

    d2=np.array([
         8.0000000000000014e+001,
         3.7916666666666652e+000,
        -1.5374999999999993e-002,
         1.5833333333333326e-005
    ])
    d1=np.array([
         3.0000000000000000e+002,
         4.4583333333333339e+000,
        -2.0625000000000001e-002,
         2.516666666666667e-005
    ])
    m=map.Map(size,d1,d2)

    screen = pygame.display.set_mode(size)
    angle_difference=0
    actions = [' U',' UL',' UR',' R',' L',' D']

    genetic_algo=AI.GeneticAlgo(population_size=20,n_actions=6,input_size=16*16)
    n_trials = 10
    for t in range(int(n_trials)):
        scores = [race(model,m,graphic=False) for model in genetic_algo.population]
        print("step: "+str(t)+" max score:"+str(np.max(scores)))
        model=genetic_algo.population[np.argmax(scores)]
        race(model,m,graphic=True)
        genetic_algo.mutation(scores)
