from CommonVariables import *

class Creature:
    #initialize a creature with random coordinates, zero speed, 100 energy
    def __init__(self):
        self.x = random.uniform(0, map_size[0])
        self.y = random.uniform(0, map_size[1])
        self.speed = 0
        self.turnspeed = 0
        self.energy = 100
        self.size = 9
        self.rotation = random.uniform(0,2*math.pi)

    #move the creature according to its current speeds
    def move(self):
        self.rotation += self.turnspeed

        self.x += math.cos(self.rotation)*self.speed
        self.y += math.sin(self.rotation)*self.speed

        #ensure the creature is still inside of boundaries
        self.x = self.x % map_size[0]
        self.y = self.y % map_size[1]
        if (self.x < 0):
            self.x += map_size[0]
        if (self.y < 0):
            self.y += map_size[1]

    #this function is a placeholder, we will later on put the AI here to choose behaviors based on stuff
    def changeBehavior(self):
        self.speed += random.uniform(-0.5,0.5)
        self.turnspeed += random.uniform(-0.05,0.05)


    #this function ensures the creatures are never moving too fast
    def bound(self):
        np.clip(self.speed, 0, maxspeed)
        np.clip(self.turnspeed, -maxturnspeed, maxturnspeed)