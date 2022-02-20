from CommonVariables import *
from Creature import *
from Map import *
from Renderer import *
import time

m = Map(0,0)

while(True):
    m.updateMap()
    renderMap(m)
    time.sleep(0.1)
