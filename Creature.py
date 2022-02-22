from CommonVariables import *

class Creature:
    #initialize a creature with random coordinates, zero speed, 100 energy
    def __init__(self):
        self.x = random.uniform(0, map_size[0])
        self.y = random.uniform(0, map_size[1])
        self.speed = 0
        self.turnspeed = 0
        self.energy = 100
        self.size = creaturesize
        self.rotation = random.uniform(0,2*math.pi)
        self.lifetime = 0
    

    #this function is a placeholder, we will later on put the AI here to choose behaviors based on stuff
    def changeBehavior(self):
        self.speed += random.uniform(-0.2,0.5)
        self.turnspeed += random.uniform(-0.05,0.05)


    #move the creature according to its current speeds
    def move(self):
        self.rotation += self.turnspeed

        self.x += math.cos(self.rotation)*self.speed
        self.y += math.sin(self.rotation)*self.speed

        #lose some speed, always
        self.speed *= 0.95
        self.turnspeed *= 0.95

        #keep speed within certain boundaries
        self.speed = np.clip(self.speed, 0, maxspeed)
        self.turnspeed = np.clip(self.turnspeed, -maxturnspeed, maxturnspeed)

        #ensure the creature stays on the map
        self.x = self.x % map_size[0]
        self.y = self.y % map_size[1]
        if (self.x < 0):
            self.x += map_size[0]
        if (self.y < 0):
            self.y += map_size[1]
        
        #lose energy based on speed and a flat value
        self.energy -= (self.speed+self.turnspeed+1)/fps
        self.lifetime += 1/fps
