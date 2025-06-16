from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        self.root = Tk()  #creates main root window an instance of Tk
        self.root.title("Maze Solver") #this .title() method is alreadt part of the Tk class
        
        self.screen = Canvas(self.root, bg = "white",  width = self.width, height = self.height)
        self.screen.pack(fill = BOTH, expand = 1)  #pack already a method of Canvas class places the screen
        self.is_running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close(self):
        self.is_running = True
        while self.is_running == True:
            self.redraw()
    
    def close(self):
        self.is_running = False

    def draw_line(self, line, fill_color = "black"):
        line.draw(self.screen, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self,point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def draw(self, canvas, fill_color = "black"):
        canvas.create_line(self.point_1.x, self.point_1.y,
                           self.point_2.x, self.point_2.y, 
                           fill = fill_color, width = 2 )

