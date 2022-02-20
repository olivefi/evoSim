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
            c.move()
            c.lifetime += 0.1
            #if a creature's energy is less than 0, kill it
            if c.energy < 0:
                print("someone should die")
                self.creatures.remove(c)