from Creature import *
class Map:
    #initialize a new map with spawn rates
    def __init__(self, creaturespawnrate, foodspawnrate):
        self.creaturespawnrate = creaturespawnrate
        self.foodspawnrate = foodspawnrate
        self.creatures = []
        #spawn initial batch of creatures
        for i in range(num_creatures):
            self.creatures.append(Creature())
    
    #advance the map by one time tick
    def updateMap(self):
        for c in self.creatures:
            c.changeBehavior()
            c.bound()
            c.move()
