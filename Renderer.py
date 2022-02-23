import tkinter
import time
from CommonVariables import *
from Map import *
#set up basic window properties

class Renderer:
    def __init__(self):
        #main window
        self.window = tkinter.Tk()
        self.window.title("evoSim Renderer")

        #place the creatures will be rendered
        self.canvas = tkinter.Canvas(self.window, bg="black", width = map_size[0], height=map_size[1])
        self.canvas.pack(side=tkinter.LEFT)

        #settings section container
        self.settings_section = tkinter.LabelFrame(self.window, text="Settings")
        self.settings_section.pack(padx=10,pady=10, side=tkinter.RIGHT)


        self.speed_slider_label = tkinter.LabelFrame(self.settings_section, text="Simulation Speed")
        self.speed_slider_label.pack(padx=10,pady=10)

        self.speed_slider = tkinter.Scale(self.speed_slider_label, from_=1, to=5.0, orient='horizontal')
        self.speed_slider.pack()

        self.simspeed = 1.

    def renderMap(self, map):
        #get rid of all previously rendered creatures
        self.canvas.delete("creatures","food")

        #render food
        for f in map.food:
            self.canvas.create_oval(f.x + f.size, f.y+f.size, f.x-f.size, f.y - f.size, fill="green",tags="food")

        #create triangles symbolizing the creatures
        for c in map.creatures:
            triangle = [c.x+c.size*math.cos(c.rotation-math.pi*2/3),c.y+c.size*math.sin(c.rotation-math.pi*2/3), c.x+c.size*math.cos(c.rotation+math.pi*2/3),c.y+c.size*math.sin(c.rotation+math.pi*2/3), c.x+2*c.size*math.cos(c.rotation),c.y+2*c.size*math.sin(c.rotation)]
            self.canvas.create_polygon(triangle, fill="white",tags="creatures")
        
        #update, wait according to fps
        self.window.update_idletasks()
        self.window.update()
        time.sleep(1/(fps*self.simspeed))


    def updateSliders(self):
        self.simspeed = self.speed_slider.get()