import tkinter
from Map import *
#set up basic window properties

window = tkinter.Tk()
window.title("evoSim Renderer")

canvas = tkinter.Canvas(window, bg="black", width = map_size[0], height=map_size[1])

canvas.pack(expand=True, fill="both")

def renderMap(map):
    #get rid of all previously rendered creatures
    canvas.delete("creatures")
    for c in map.creatures:
        #create a triangle symbolizing the creature
        triangle = [c.x+c.size*math.cos(c.rotation-math.pi*2/3),c.y+c.size*math.sin(c.rotation-math.pi*2/3), c.x+c.size*math.cos(c.rotation+math.pi*2/3),c.y+c.size*math.sin(c.rotation+math.pi*2/3), c.x+2*c.size*math.cos(c.rotation),c.y+2*c.size*math.sin(c.rotation)]
        canvas.create_polygon(triangle, fill="white",tags="creatures")
        window.update_idletasks()
