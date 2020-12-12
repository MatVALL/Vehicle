import vehicle, map, AI

won=0
lost=0

def apply_action(v,action):
    acceleration=0
    angle_difference=0
    if 'U' in action:
        v.acceleration=8
    if 'B' in action:
        v.acceleration=-4
    if 'L' in action:
        angle_difference=1
    if 'R' in action:
        angle_difference=-1
    v.angle += angle_difference*v.getSpeed()/3
    v.move()

def calculateReward(v,m):
    reward = -1
    global lost
    global won
    if m.positionIsGoal((v.x,v.y)):
        won = won + 1
        reward = 100
    if not m.positionIsValid((v.x,v.y)):
        lost= lost+1
        return -100
    return reward

def gameIsOver(v,m):
    return not m.positionIsValid((v.x,v.y)) or m.positionIsGoal((v.x,v.y))
