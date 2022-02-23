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
            self.food.append(Food())
    
    #advance the map by one time tick
    def updateMap(self):
        for c in self.creatures:
            c.changeBehavior()
            c.move()
            c.eat(self.food)
            #if a creature's energy is less than 0, kill it
            if c.energy < 0:
                self.creatures.remove(c)
        
        