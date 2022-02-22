from CommonVariables import *
from Creature import *
from Map import *
from Renderer import *
import time

m = Map(0,0)
r = Renderer()
while(True):
    m.updateMap()
    r.updateSliders()
    r.renderMap(m)
