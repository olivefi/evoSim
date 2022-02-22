from Creature import *
from Food import *

class Map:
    #initialize a new map with spawn rates and empty food, creature lists
    def __init__(self, creaturespawnrate, foodspawnrate):
        self.creaturespawnrate = creaturespawnrate
        self.foodspawnrate = foodspawnrate
        self.creatures = []
        self.food = []
        #spawn initial batch of creatures
        for i in range(num_creatures):
            self.creatures.append(Creature())

    def foodInRange(self, c):
        eatablefood = []
        for f in self.food:
            #if distance between creature and a piece of food on the map is less than eatable, add it to "eatable" list
            if (math.sqrt(math.pow(c.x - f.x,2)+math.pow(c.y - f.y,2)) < eatingrange):
                eatablefood.append(f.index())
        return eatablefood
    
    #advance the map by one time tick
    def updateMap(self):
        for c in self.creatures:
            c.changeBehavior()
            c.move()
            eatablefood = self.foodInRange(c)
            for e in eatablefood:
                self.food[e].remove()
                c.energy += 5
            #if a creature's energy is less than 0, kill it
            if c.energy < 0:
                self.creatures.remove(c)


