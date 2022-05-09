## AUTHOR: Alexandra Bacula
## ENG 103 Week 6 Assignment

import numpy as np
import random
import turtle
import time
from matplotlib import cm

turtle.Turtle()
### If you want to change the speed the turtle moves at, do so here ###
turtle.speed(speed='fast')

#### EXAMPLE 1 FUNCTION ####
def example_overlapping_stars(n, x, angle):
    # SOURCE: https://www.geeksforgeeks.org/draw-colourful-star-pattern-in-turtle-python

    # loop for number of stars
    for i in range(n):

        # Set it so that colors are set as RGB values
        turtle.colormode(255)

        # choosing random integers
        # between 0 and 255
        # to generate random rgb values
        a = random.randint(0, 255)
        b = random.randint(0, 255)
        c = random.randint(0, 255)

        # setting the outline in RGB
        # and fill colour in RGB
        turtle.pencolor(a, b, c)
        turtle.fillcolor(a, b, c)

        # begins filling the star
        turtle.begin_fill()

        # loop for drawing each star
        for j in range(5):
            turtle.forward(5 * n - 5 * i)
            turtle.right(x)
            turtle.forward(5 * n - 5 * i)
            turtle.right(72 - x)

        # colour filling complete
        turtle.end_fill()

        # rotating for
        # the next star
        turtle.rt(angle)


#### EXAMPLE 2 FUNCTION ####
def example_rainbow_spiral(n):
    ### SOURCE: https://www.geeksforgeeks.org/turtle-programming-python

    # list of six colors for the line color
    # colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
    colors = cm.get_cmap(cm.viridis,6)
    print(colors(0))

    # Call the turtle pen
    t = turtle.Pen()

    # set the background color
    turtle.bgcolor('black')

    for x in range(n):
        # Change the pen color
        t.pencolor((np.clip(colors(x),2,10)-2)/8.)

        # Change the pen line width based on n
        t.width(x//100 + 1)

        # Move forward x amount
        t.forward(x)

        # Rotate 59 deg left
        t.left(59)

###################
#### EDIT HERE ####
###################

### WRITE YOUR TWO FUNCTIONS USING THE TURTLE LIBRARY


###########################
#### STOP EDITING HERE ####
###########################

if __name__ == '__main__':
    ################ EXAMPLE 1 ###################
    ## This example draws n stars of different colors at different rotation angles
    ## COMMENT THIS OUT IF YOU DONT WANT THE EXAMPLES TO RUN

    # setting the inputs
    # n = 3  # number of stars
    # x = 144  # exterior angle of each star
    # angle = 18  # angle of rotation for the spiral
    #
    # # call the function
    # example_overlapping_stars(n,x,angle)
    # # Reminder to screenshot the output
    # print('SCREENSHOT NOW!')
    # # Pause for 30 seconds after the output is drawn so the user can screenshot
    # time.sleep(30)
    # # # Clear the turtle plot
    # turtle.clear()
    #
    # ############ END EXAMPLE 1 ###################
    #
    # ################ EXAMPLE 2 ###################
    # ## This example draws n stars of different colors at different rotation angles

    # setting the inputs
    n = 100

    # call the function
    example_rainbow_spiral(n)
    # Reminder to screenshot the output
    print('SCREENSHOT NOW!')
    # Pause for 30 seconds after the output is drawn so the user can screenshot
    time.sleep(30)
    # Clear the turtle plot
    turtle.clear()



    ############ END EXAMPLE 2 ###################

    ###################
    #### EDIT HERE ####
    ###################

    ### Call your custom functions here
    ## Recommended to use time.sleep to pause after calling the function for screenshotting purposes


