## AUTHOR: Alexandra Bacula
## ENG 103 base code 2

import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection
from matplotlib.backend_bases import MouseButton


class eng103_base2:

    # This is the initialization function of the class
    def __init__(self):
        # Initialize the figure and set the size
        self.fig, self.ax = plt.subplots(figsize=(5, 5))

        # Set the axis limits
        self.ax.set(xlim=(-10, 10), ylim=(-10, 10))

        # Initialize the patches list
        self.patches = []

    # This function draws a static rectangle
    ## INPUTS: x, y, height, width
    ## OUTPUTS: rectangle centered at (x,y) of given dimensions
    def draw_static_rectangle(self,x,y,height,width):
        # add a rectangle
        rect = mpatches.Rectangle((x,y), width, height,ec="none")
        self.patches.append(rect)

    # This function draws a static circle
    ## INPUTS: x, y, radius
    ## OUTPUTS: circle centered at (x,y) of given radius
    def draw_static_circle(self,x,y,radius):
        # add a circle
        circle = mpatches.Circle((x,y), radius, ec="none")
        self.patches.append(circle)

    # This function draws a static ellipse
    ## INPUTS: x, y, width, height, tilt
    ## OUTPUTS: ellipse centered at (x,y) of given dimensions
    def draw_static_ellipse(self,x,y,width,height,tilt):
        # add an ellipse
        ellipse = mpatches.Ellipse((x,y),width,height,angle=tilt)
        self.patches.append(ellipse)

    # This function is triggered when the mouse is clicked
    def get_mouse_coords(self,event):
        # Reset patches so every shape isn't redrawn at every click
        self.patches = []
        # If the left mouse button is clicked
        if event.button is MouseButton.LEFT:
            # get the x and y pixel coords of the click
            x, y = event.x, event.y
            # If the coordinates are in the figure range
            if event.inaxes:
                ax = event.inaxes  # the axes instance
                flag = 0

                # Prompt user to input the shape
                print("What shape? ")
                # Save the user's input
                shape = input()

                # If the user input "rectangle"
                if shape == 'rectangle':
                    # Prompt the user to input the desired width
                    print("Width?")
                    # Save the input as a float
                    width = float(input())
                    # Prompt the user to input the desired height
                    print("Height?")
                    # Save input as a float
                    height = float(input())
                    self.draw_static_rectangle(event.xdata-(width/2), event.ydata-(height/2), height, width)

                elif shape == 'circle':
                    print("Radius?")
                    radius = float(input())
                    self.draw_static_circle(event.xdata, event.ydata, radius)

                elif shape == 'ellipse':
                    print("Width?")
                    width = float(input())
                    print("Height?")
                    height = float(input())
                    print("Tilt? (range 0:180)")
                    tilt = float(input())
                    self.draw_static_ellipse(event.xdata,event.ydata,width,height,tilt)

                else:
                    print("Not a supported shape!")
                    flag = 1
                if flag == 0:
                    print("Color?")
                    color = input()
                    print("Opactiy? (range 0:1)")
                    opacity = float(input())
                    p = PatchCollection(self.patches, alpha=opacity)
                    p.set_facecolor(color)
                    self.ax.add_collection(p)
                    plt.show()
                    plt.savefig('test_point_click_studio3.png')
                print("Click where you want the next shape!")



if __name__ == '__main__':
    # Call the class
    ## Classes are a way to organize code, variables, and functions.
    ## For ENG 103, we will not be learning about classes, but you are welcome to look into them on your own.
    base2 = eng103_base2()

    base2.draw_static_circle(0, 0, 0.01)
    p = PatchCollection(base2.patches, alpha=0.1)
    base2.ax.add_collection(p)

    # The fig.show() function shows the figure in a separate window on your screen
    base2.fig.show()
    plt.title("Alexandra Bacula, Studio 3 Solution")
    plt.pause(1)


    print("Click where you want the shape!")
    plt.connect('button_press_event', base2.get_mouse_coords)



    plt.show()
    plt.pause(1)

