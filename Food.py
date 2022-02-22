from CommonVariables import *

class Food:
    def __init__(self):
        self.x = random.uniform(0, map_size[0])
        self.y = random.uniform(0, map_size[1])