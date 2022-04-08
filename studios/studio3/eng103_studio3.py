## AUTHOR: Alexandra Bacula
## ENG 103 studio 3 code

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection
from matplotlib.backend_bases import MouseButton


class eng103_studio3:

    # This is the initialization function of the class
    def __init__(self):
        # Initialize the figure and set the size
        self.fig, self.ax = plt.subplots(figsize=(5, 5))

        # Set the axis limits
        self.ax.set(xlim=(-10, 10), ylim=(-10, 10))

        # Initialize the patches list
        self.patches = []

    ################ SHAPE FUNCTIONS #####################
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
    def draw_static_ellipse(self,x,y,height,width,tilt):
        # add an ellipse
        ellipse = mpatches.Ellipse((x,y),width,height,angle=tilt)
        self.patches.append(ellipse)

    ################ INTERACTIVITY FUNCTION #####################
    # This function is triggered when the mouse is clicked
    def interactive_plot(self,event):
        # Reset patches so every shape isn't redrawn at every click
        self.patches = []
        # If the left mouse button is clicked
        if event.button is MouseButton.LEFT:
            # get the x and y pixel coords of the click
            x, y = event.xdata, event.ydata
            # If the coordinates are in the figure range
            if event.inaxes:
                ax = event.inaxes  # the axes instance
                flag = 0

                # Prompt user to input the shape
                print("What shape? Choose from [rectangle, circle, ellipse]")
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
                    self.draw_static_rectangle(x-(width/2), y-(height/2), height, width)

                elif shape == 'ellipse':
                    print("Width?")
                    width = float(input())
                    print("Height?")
                    height = float(input())
                    print("Tilt? (range 0:180)")
                    tilt = float(input())
                    self.draw_static_ellipse(x,y,height,width,tilt)

                ##### EDIT HERE ######

                # Write an additional elif statement for drawing a circle when the input is 'circle'
                # Using the examples above from rectangle and ellipse, ask the user for the radius of the circle
                ## This will consist of one print statement, and saving the input as a float type variable called radius

                # Then, call the draw_static_circle() function
                ## Use the examples from the rectangle and ellipse function calls in lines 78 and 87
                ## The circle function will take in the x and y position like the rectangle and ellipse, and will also take in the radius

                ##### STOP EDITING HERE #####

                elif shape == 'Done' or shape == 'Finished':
                    flag = 1
                    self.exit_loop = 1
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

                    ##### EDIT HERE #####
                    # Change this to whatever you want to save your png as
                    ## Remember to change it every time you want a new png, otherwise the code will overwrite the old one
                    plt.savefig('test_point_click_studio3.png')
                    ##### STOP EDITING HERE

                print("Click where you want the next shape!")

    ########## STUDIO 3 PART 1 #############
    def studio3_part1(self):
        # EXAMPLE CIRCLE #
        ## Plot the circle at (0,0) with radius of 1
        self.draw_static_circle(0, 0, 1)
        ## Set the opacity of the shape to 0.5
        p = PatchCollection(self.patches, alpha=0.5)
        ## Set the color of the shape to lavender
        p.set_facecolor('lavender')
        ## Add the patch to the list of patches
        self.ax.add_collection(p)
        ## Clear patches so we don't overwrite color choices
        self.patches = []

        ##### EDIT HERE #####
        # Plot at least three more shapes on the plot.
        # The axes limits are x: -10 to 10, y: -10 to 10
        # Use the example circle above to add shapes to the plot

        ## First choose your shape and call one of the following functions:
        ## Be sure to fill in the x,y center position and the dimensions
        ### RECTANGLE: self.draw_static_rectangle(center x, center y, height, width)
        ### CIRCLE:    self.draw_static_circle(center x, center y, radius)
        ### ELLIPSE:   self.draw_static_ellipse(center x, center y, height, width, tilt)

        ## Next, decide how see-through you want your shape
        ## 0 is fully see-through and 1 is fully solid
        ## Set alpha equal to that value in the following function:
        ### COPY AND FILL IN ALPHA: p = PatchCollection(self.patches, alpha=0.5)

        ## Then, chose the color you want your shape to be
        ## Replace 'lavender' in the example with your color in the following function:
        ### COPY AND FILL IN COLOR: p.set_facecolor('lavender')

        ## Finally, copy the following two functions, but don't change anything about them
        ## The first function is adding the shape you just specified to the list of shapes to plot
        ## The second is clearing your patches so that you don't overwrite your color and opacity choices
        ### COPY AND DO NOT CHANGE: self.ax.add_collection(p)
        ### COPY AND DO NOT CHANGE: self.patches = []

        ## PUT YOUR SHAPES HERE
        ## Each shape requires all five lines of code in the order specified above


        # Change this to your name and your PNG name
        plt.title("Alexandra Bacula, Studio 3 Part 1")
        plt.savefig('bacula_studio3_part1.png')
        ##### STOP EDITING HERE #####

        plt.show()

    ########## STUDIO 3 PART 2 #############
    def studio3_part2(self):
        self.draw_static_circle(0, 0, 0.01)
        p = PatchCollection(self.patches, alpha=0.1)
        self.ax.add_collection(p)

        # Turn on interactive mode
        plt.ion()

        # The fig.show() function shows the figure in a separate window on your screen
        self.fig.show()

        ##### EDIT HERE #####
        # Change this to your name
        plt.title("Alexandra Bacula, Studio 3 Part 2")
        ##### STOP EDITING HERE #####

        # Pause so the plot doesn't close
        plt.pause(1)

        # Prompt the user to click on the plot where they want the shape
        print("Click where you want the shape!")
        # On mouse click, run the interactive_plot function
        plt.connect('button_press_event', self.interactive_plot)

        # Show the plot
        plt.show(block = True)
        plt.pause(1)

if __name__ == '__main__':
    # Call the class
    ## Classes are a way to organize code, variables, and functions.
    ## For ENG 103, we will not be learning about classes, but you are welcome to look into them on your own.
    studio3 = eng103_studio3()

    #### EDIT HERE ####
    # Change between studio3.studio3_part1() and stuido3.studio3_part2()
    studio3.studio3_part1()


