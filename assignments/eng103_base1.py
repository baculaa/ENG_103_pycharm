## AUTHOR: Alexandra Bacula
## ENG 103 base code 1

import csv
import numpy as np
import matplotlib.pyplot as plt


class eng103_base1:

    # This is the initialization function of the class
    def __init__(self):
        # Initialize the figure
        self.fig, self.ax = plt.subplots(figsize=(10, 10))
        # Set the axis limits
        self.ax.set(xlim=(-3, 3), ylim=(-1, 1))

        # Initialize the x and y data lists so we can edit them later
        self.data_x = []
        self.data_y = []

    # This is a custom function created to read in the CSV file data.
    ## Inputs: the CSV file name
    ## Outputs: two python lists: one with the x data and one with the y data
    def read_in_data(self,filename):

        ## We start by opening the file
        with open(filename) as file_name:
            ## Then we use the csv.reader() function to allow python to read the data
            file_read = csv.reader(file_name)
            # Next, we go through each row of the data and pull out the x point and the y point
            for row in file_read:
                # We add the x point to a list of the x points
                self.data_x.append(float(row[0]))
                # We add the y point to a list of the y points
                self.data_y.append(float(row[1]))

    # This is a custom function that changes the color of a plotted point
    ## INPUT: the index of the current point being plotted in the main function
    ## OUTPUT: the color of the point
    def set_colors_assignment_1(self,n):
        # ASSIGNMENT 1:

        ##### EDIT HERE ######

        ## Change the color of the point to something else
        ## See here for color options: https://matplotlib.org/stable/gallery/color/named_colors.html

        # This variable sets the fill color of the marker
        marker_fill_color = 'black'

        # This variable sets the edge color of the marker
        marker_edge_color = 'black'

        # This variable sets the marker size
        marker_size = 10

        # This variable sets the marker style
        ## see here for the possible marker types: https://matplotlib.org/3.5.1/gallery/lines_bars_and_markers/marker_reference.html
        marker_type = 'o'

        # If you want your marker to be half one color and half another, choose a second color
        marker_fill_color2 = 'lightsteelblue'

        # And choose how you want to split your marker colors
        ## options: 'full' , 'left' , 'right' , 'bottom' , 'top' , 'none'
        marker_fill_style = 'full'

        ##### STOP EDITING HERE #####
        ### DO NOT EDIT BELOW THIS LINE!! ###
        marker_style = dict(marker=marker_type, markerfacecolor=marker_fill_color, markerfacecoloralt=marker_fill_color2,
                            markersize=marker_size, markeredgecolor=marker_edge_color, fillstyle=marker_fill_style)

        return marker_style

        #####################################################################################
    def set_colors_assignment_2(self,n):

        # ASSIGNMENT 2:
        ## Write your if else statements to change the color of the points based on something
        ## For ex. distance from center, angle around a circle, index number, etc
        ## Since we have numpy imported, look up numpy functions to do any math you need
        ## When you call numpy functions, you will need to put np. before the function
        ### For ex. np.sqrt() will give you the square root of a number

        # HINTS: Below are some examples of points and x and y points. We provide:
        ## A sample point at (0,0) as a numpy array
        ## The sample point x value as a float
        ## The sample point y value as a float
        ## The current point as a numpy array
        ## The current x value as a float
        ## The current y value as a float

        # This is an example of how to create a point using numpy. This point is (0,0).
        ## To change this point, just change the numbers.
        ## To create an additional point for comparison:
        #### (1) copy and paste the line
        #### (2) change the name of the variable from base_point to something else
        #### (3) change the value of the points to whatever you like
        base_point = np.array((0, 0))

        # This is the base point x value
        base_x = 0

        # This is the base point y value
        base_y = 0

        # This is the current point we are plotting from the data
        ## It is saved as a numpy array
        current_point = np.array((self.data_x[n], self.data_y[n]))

        # This is the current x value
        current_x = self.data_x[n]

        # This is the current y value
        current_y = self.data_y[n]

        ##### EDIT HERE #####
        ###### WRITE YOUR IF/ELSE STATEMENT HERE ######

        ### DO NOT EDIT BELOW THIS LINE!! ###
        marker_style = dict(marker=marker_type, markerfacecolor=marker_fill_color, markerfacecoloralt=marker_fill_color2,
                            markersize=marker_size, markeredgecolor=marker_edge_color, fillstyle=marker_fill_style)

        return marker_style


# This is the main function. Do not change anything about this line.
if __name__ == '__main__':

    # Call the class
    ## Classes are a way to organize code, variables, and functions.
    ## For ENG 103, we will not be learning about classes, but you are welcome to look into them on your own.
    base1 = eng103_base1()

    ##### EDIT HERE ######
    ## Change the filename to read in the provided csv file
    base1.read_in_data('[FILENAME GOES HERE]')

    # This variable looks at the data and determines how many points there are
    data_length = len(base1.data_x)

    # Now we go through every point in the data
    for n in range(data_length):

        # The set_colors() function is a custom function that sets the color for a point in the data with a given index n
        ## This function is defined in the code above and the color will be edited there
        marker_style = base1.set_colors_assignment_1(n)

        # This is where we plot the current point on the scatter plot
        ## n denotes the index of the (x,y) point we are currently plotting
        ## The input color=[name of color or variable containing color] changes the color of the point
        base1.scatter_plot = base1.ax.scatter(base1.data_x[n], base1.data_y[n], **marker_style)

        # The fig.show() function shows the figure in a separate window on your screen
        base1.fig.show()

        ##### EDIT HERE ######

        # This function sets the background color of the plot
        ## Change the color to a color of your choice
        base1.ax.set_facecolor("white")

        # The function plt.title() sets the title of the plot
        ## Change the title to your name and the assignment number
        plt.title("[YOUR NAME, ASSIGNMENT X]")
        ##### STOP EDITING HERE #####

        # The plt.pause() function pauses the plot from closing for the number of seconds in the parentheses
        plt.pause(0.05)

    ##### EDIT HERE ######
    # Add in the name of your png below
    plt.savefig('[FILENAME].png')
    ##### STOP EDITING HERE #####

    # The fig.show() function shows the figure in a separate window on your screen
    base1.fig.show()
    # The plt.pause() function pauses the plot from closing for the number of seconds in the parentheses
    plt.pause(10)

