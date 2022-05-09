## AUTHOR: Alexandra Bacula


import csv
import numpy as np
import PIL
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection
from matplotlib.backend_bases import MouseButton
from matplotlib import animation as anim
import time as timepack
import sounddevice as sd
import random
import turtle
import time


class interactive_plotting:
    # This is the initialization function of the class
    def init_figure(self):
        # Initialize the figure and set the size
        self.fig, self.ax = plt.subplots(figsize=(5, 5))

        # Set the axis limits
        self.ax.set(xlim=(-10, 10), ylim=(-10, 10))

        # Initialize the patches list
        self.patches = []

        #Init mouse click location
        self.mouse_x = 0
        self.mouse_y = 0

    # This function draws a static rectangle
    ## INPUTS: x, y, height, width
    ## OUTPUTS: rectangle centered at (x,y) of given dimensions
    def draw_static_rectangle(self, x, y, height, width):
        # add a rectangle
        rect = mpatches.Rectangle((x, y), width, height, ec="none")
        self.patches.append(rect)

    # This function draws a static circle
    ## INPUTS: x, y, radius
    ## OUTPUTS: circle centered at (x,y) of given radius
    def draw_static_circle(self, x, y, radius):
        # add a circle
        circle = mpatches.Circle((x, y), radius, ec="none")
        self.patches.append(circle)

    # This function draws a static ellipse
    ## INPUTS: x, y, width, height, tilt
    ## OUTPUTS: ellipse centered at (x,y) of given dimensions
    def draw_static_ellipse(self, x, y, width, height, tilt):
        # add an ellipse
        ellipse = mpatches.Ellipse((x, y), width, height, angle=tilt)
        self.patches.append(ellipse)

    # This function is triggered when the mouse is clicked and saves the x and y location
    def get_mouse_coords(self, event):

        # If the left mouse button is clicked
        if event.button is MouseButton.LEFT:
            # get the x and y pixel coords of the click
            self.mouse_x, self.mouse_y = event.x, event.y

    def click_and_user_specify_shape_helper(self,event):
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
                    self.draw_static_rectangle(event.xdata - (width / 2), event.ydata - (height / 2), height, width)

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
                    self.draw_static_ellipse(event.xdata, event.ydata, width, height, tilt)
                elif shape == 'Done' or shape == 'Finished':
                    flag = 1
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

                print("Click where you want the next shape!\n Type done or finished if you are finished")

    # Studio 3 where you click on the plot and the user specifies the shape type/color/size
    # Inputs: none
    # Outputs: plot with shapes
    def click_and_user_specify_shape(self):
        self.draw_static_circle(0, 0, 0.01)
        p = PatchCollection(self.patches, alpha=0.1)
        self.ax.add_collection(p)

        # The fig.show() function shows the figure in a separate window on your screen
        plt.ion()
        self.fig.show()

        ##### EDIT HERE #####
        # Change this to your name
        plt.title("Alexandra Bacula, Studio 3 Part 2")
        ##### STOP EDITING HERE #####

        plt.pause(1)
        print("Click where you want the shape!")
        plt.connect('button_press_event', self.click_and_user_specify_shape_helper)

        plt.show(block=True)
        plt.pause(1)

    ## This function plots the arrangement of paintings on a wall.
    ## Inputs: Wall length/height, painting length/height, number of paintings
    ## Outputs: Plot of wall (No values returned)
    def Plot_Paintings(self, Wall_Length, Painting_Length, Num_Paintings, Wall_Height, Painting_Height):

        ##   HOUSEKEEPING FOR PLOTS   ##
        plt.ion()  # Turn on interactive mode -- this way your plot updates when you add new things
        plt.xlim([-0.2 * Wall_Length, 1.2 * Wall_Length])
        plt.ylim([-0.5 * Wall_Height, 1.5 * Wall_Height])
        plt.gca().set_aspect(1)  # Keep aspect ratio equal (don't stretch the plot)
        Plot_StickFigure()
        # ________________________________

        # ________________________________
        ##   PLOT THE WALL ITSELF   ##
        ##   ! USE THIS ! as a reference when you write your code below
        Wall_Corners = Find_Corners(Center_X=Wall_Length / 2, Center_Y=Wall_Height / 2, Span_X=Wall_Length,
                                    Span_Y=Wall_Height)  # Find corners using call to function "Find_Corners"
        plt.plot(Wall_Corners[:, 0], Wall_Corners[:, 1], linewidth=2,
                 color='black')  ## Plot the wall (as lines connecting its corners)
        plt.fill(Wall_Corners[:, 0], Wall_Corners[:, 1], color='lightcyan')  ## Fill the wall with color
        plt.waitforbuttonpress()  ## Display the plot and wait until a button is pressed before continuing
        # ________________________________


        Painting_req_space = Painting_Length * Num_Paintings

        if Painting_req_space >= Wall_Length:
            print("Oh no bad your paintings wont fit")
        else:
            print("Yay they fit")

        Spacing = (Wall_Length - (Painting_Length * Num_Paintings)) / (
                    Num_Paintings + 1)  ## Calculate Spacing between paintings

        # ________________________________
        ##   PLOT EACH PAINTING IN FOR LOOP  ##
        for Painting in range(Num_Paintings):
            ###################################################

            X_Position = Spacing * (Painting + 1) + Painting_Length * (
                        1 / 2 + Painting)  ## Calculate X coordinate marking center of painting
            Corners = Find_Corners(Center_X=X_Position, Center_Y=Wall_Height / 2, Span_X=Painting_Length,
                                   Span_Y=Painting_Height)  ## Find corners using call to function "Find Corners"
            plt.plot(Corners[:, 0], Corners[:, 1],
                     color='black')  ## Plot the corners in the defined order (the order has already been defined outside of the loop)
            # Color = np.array([np.cos(2*np.pi*-Painting/(Num_Paintings*1.2)),np.cos(2*np.pi*(-Painting/(Num_Paintings*1.2) +1/3)),np.cos(2*np.pi*(-Painting/(Num_Paintings*1.1) +2/3))])/2+0.5
            plt.fill(Corners[:, 0], Corners[:, 1], color='blue')
            plt.waitforbuttonpress()  ## Display the plot and wait until a button is pressed before continuing


    ## This plots a stick figure to stare at your wall full of art
    # Inputs: x and y offest (where you want your stick figure)
    # Outputs: stick figure will be plotted
    def Plot_StickFigure(self, Offset_x, Offset_y):

        ## This plots a stick figure to stare at your wall full of art

        Vertices = np.array([[-0.05443548, 0.49188312],
                             [-0.10685484, 0.47294372],
                             [-0.18548387, 0.52705628],
                             [-0.22782258, 0.71103896],
                             [-0.18951613, 0.84361472],
                             [-0.07459677, 0.91125541],
                             [0.09677419, 0.92478355],
                             [0.13508065, 0.82467532],
                             [0.125, 0.5974026],
                             [0.08669355, 0.47835498],
                             [0.01209677, 0.4702381],
                             [-0.02620968, 0.49458874],
                             [-0.02419355, 0.14015152],
                             [0.34072581, -0.08170996],
                             [-0.03024194, 0.14285714],
                             [-0.41935484, 0.10497835],
                             [-0.02217742, 0.14015152],
                             [-0.01008065, -0.38744589],
                             [0.25806452, -0.77435065],
                             [0.43951613, -0.7797619],
                             [0.26209677, -0.7797619],
                             [-0.01209677, -0.3982684],
                             [-0.01209677, -0.39556277],
                             [-0.23790323, -0.76623377],
                             [-0.45766129, -0.75811688]])
        plt.plot(Vertices[:, 0] + Offset_x, Vertices[:, 1] + Offset_y)

    # This returns the corners of a rectangle for which the center and span are provided.
    ## Inputs: Center of rectangle (X and Y) and dimensions/span (X and Y).
    ## Outputs: Corners of rectangle as array
    def Find_Corners(self, Center_X, Center_Y, Span_X, Span_Y):

        #
        # ________________________________

        Upper_Left = (Center_X - Span_X / 2, Center_Y + Span_Y / 2)
        Upper_Right = (Center_X + Span_X / 2, Center_Y + Span_Y / 2)
        Lower_Left = (Center_X - Span_X / 2, Center_Y - Span_Y / 2)
        Lower_Right = (Center_X + Span_X / 2, Center_Y - Span_Y / 2)
        Corners = [Upper_Left, Upper_Right, Lower_Right, Lower_Left, Upper_Left]
        return np.array(Corners)

class data_reading:

    # Read in the CSV file data, CSV must have one x,y value pair in each row with no headers
    ## Inputs: the CSV file name
    ## Outputs: two python lists: one with the x data and one with the y data
    def read_in_data(self, filename):
        data_x = []
        data_y = []
        ## We start by opening the file
        with open(filename) as file_name:
            ## Then we use the csv.reader() function to allow python to read the data
            file_read = csv.reader(file_name)
            # Next, we go through each row of the data and pull out the x point and the y point
            for row in file_read:
                # We add the x point to a list of the x points
                data_x.append(float(row[0]))
                # We add the y point to a list of the y points
                data_y.append(float(row[1]))
        return data_x, data_y

class image_manipulation:

    # Imports image from file
    # Inputs: file path for image file
    # Outputs: PIL Image
    def Import_Image(self, FileName):
        # Imports the image
        My_Image = PIL.Image.open(FileName)
        return My_Image

    # Turns image gray
    # Inputs: PIL Image
    # Outputs: Gray PIL Image
    def Gray_Image(selfself, Image):
        Gray_Image = Image.convert("LA")
        return Gray_Image

    # Shows the image until closed by the user
    # Inputs: PIL Image
    # Outputs: None
    def show_image(self, Image):
        # # Show the combined image
        plt.imshow(Image)
        # # Wait until the image is closed to continue
        plt.waitforbuttonpress()

    # Flips image around the x-axis (turns it upside down)
    # Inputs: PIL Image
    # Outputs: Flipped PIL Image
    def Flip_Image(self, Image):

        # Turn image into an array
        Image_Array = np.array(Image)

        # Get the x and y dimensions of the image
        XDim = Image_Array.shape[0]
        YDim = Image_Array.shape[1]

        # Create array of zeros of the same size as the original image
        # The zeros will be overwritten
        Flipped_Image_Array = np.zeros(Image_Array.shape)

        # Go through each pixel in X and Y
        for x in range(XDim):
            for y in range(YDim):

                # Save the pixel value of the original image to the opposite X value in the Flipped_Image_Array

                # The Image_Array is indexed as follows: Image_Array[x,y,:]
                ### The colon is there bcause there are three values in that last spot (RGB)
                ####The color lets you save all three at once

                Flipped_Image_Array[XDim - x - 1, y, :] = Image_Array[x, y, :]


        # This converts your array back into an image with the correct value type
        Flipped_Image = PIL.Image.fromarray((Flipped_Image_Array).astype(np.uint8))

        # Return the flipped image
        return Flipped_Image

    # Inverts the color of an image
    # Inputs: PIL Image
    # Outputs: Inverted color PIL Image
    def Invert_Color(self, Image):

        # Turn image into an array
        Image_Array = np.array(Image)

        # Get the x and y dimensions of the image
        XDim = Image_Array.shape[0]
        YDim = Image_Array.shape[1]

        # Create array of zeros of the same size as the original image
        # The zeros will be overwritten
        Invert_Color_Array = np.zeros(Image_Array.shape)

        # Go through each pixel in X and Y
        for x in range(XDim):
            for y in range(YDim):

                # Save the R,G,and B pixel value of the original image to 255-original value in the Combined_Image_Array
                ## Specifying each new R, G, B value

                # The Image_Array is indexed as follows:
                ### Image_Array[x,y,0] is R
                ### Image_Array[x,y,1] is G
                ### Image_Array[x,y,2] is B
                ### The colon is there bcause there are three values in that last spot (RGB)
                ####The color lets you save all three at once

                Invert_Color_Array[x, y, 0] = 255 - Image_Array[x, y, 0]
                Invert_Color_Array[x, y, 1] = 255 - Image_Array[x, y, 1]
                Invert_Color_Array[x, y, 2] = 255 - Image_Array[x, y, 2]


        # This converts your array back into an image with the correct value type
        Invert_Color_Image = PIL.Image.fromarray((Invert_Color_Array).astype(np.uint8))

        # Return the flipped image
        return Invert_Color_Image


    # Combines two images
    # Inputs: Two color PIL Image OR Two gray PIL Images
    # Outputs: Combined PIL Image
    def Combine_Images(self, Image1, Image2):
        ##################################################
        ## MAKE SURE BOTH ARE COLOR OR BOTH ARE GRAY !! ##
        ##################################################

        # Turn image into an array
        Image_Array1 = np.array(Image1)
        Image_Array2 = np.array(Image2)

        # Get the x and y dimensions of the images
        XDim1 = Image_Array1.shape[0]
        YDim1 = Image_Array1.shape[1]
        XDim2 = Image_Array2.shape[0]
        YDim2 = Image_Array2.shape[1]

        # Pick the smaller of each dimension for the combined image dimensions
        ## This will make sure we don't try to pull pixels from an index that doesn't exist
        if XDim1 <= XDim2:
            XDim = XDim1
        else:
            XDim = XDim2

        if YDim1 <= YDim2:
            YDim = YDim1
        else:
            YDim = YDim2

        # Create an array to write the combined image to with the smaller of each dimension
        ## The zeros will be overwritten
        Combined_Image_Array = np.zeros((XDim, YDim, 3))

        # Go through each pixel in X and Y
        for x in range(XDim):
            for y in range(YDim):

                # for alternating x values, get the pixel from the other image
                if x % 2 == 0:
                    Combined_Image_Array[x, y, :] = Image_Array1[x, y, :]
                else:
                    Combined_Image_Array[x, y, :] = Image_Array2[x, y, :]


        # This converts your array back into an image with the correct value type
        Combined_Image = PIL.Image.fromarray((Combined_Image_Array).astype(np.uint8))

        # Return the flipped image
        return Combined_Image

    # Compresses an image in grayscale
    # Inputs: PIL color or gray image, compression factor (how big you want the NxN blocks of pixels averaged to be)
    # Outputs: Grayscale compressed array and PIL image
    def Compress_Image(self, Image, avg_factor):

        Gray_Array = np.array(self.Gray_Image(Image))

        gray_values = Gray_Array[:, :, 0]
        XDim, YDim = gray_values.shape
        x_avg = int(XDim / avg_factor)
        y_avg = int(YDim / avg_factor)
        gray_compressed_array = np.zeros((x_avg, y_avg))

        for x in range(x_avg):
            for y in range(y_avg):
                orig_x_index = x * avg_factor
                orig_y_index = y * avg_factor
                avg_value = np.reshape(gray_values[orig_x_index:orig_x_index + avg_factor,
                                       orig_y_index:orig_y_index + avg_factor], -1)
                gray_compressed_array[x, y] = np.average(avg_value)

        gray_compressed_image = PIL.Image.fromarray(gray_compressed_array)

        return gray_compressed_array, gray_compressed_image

class sound_helpers:

    def Initialize(self):
        self.Harmonograph_Settings()
        self.Establish_Sound()
        self.Establish_Plot(Independent_Variable_Length=3200)

    def Harmonograph_Settings(self):
        ## DESCRIPTION ##
        # This function defines some settings for the Harmonograph.
        # These settings relate to a single frame of the plot, or a single note of the sound.

        # Declare global variables so they can be used in other functions without being passed as inputs
        global fx
        global fy
        global Line_Length
        global Disharmony
        global Phase_Common
        global Phase_Differential
        global Note_Titles
        global NoteHold_Steps_Per_Second
        global NoteHold_Phase_Rotation
        global NoteHold_Time
        global Graph_Update_Interval_ms
        global Base_Freq
        global Sound_Block_Size

        ## SETTINGS FOR GRAPH
        Line_Length = 18  # How many cycles to draw the trace during graphing
        Disharmony = 0 / 32  # Introduce disharmony (mismatch between fx and fy) for more interesting results
        Phase_Common = 0  # Add phase to both sinusoids
        Phase_Differential = np.pi / 4  # Add phase to only one sinusoid
        fx = 1  # Frequency tied to x axis (usually lower note)
        fy = 1  # Frequency tied to y axis (usually higher note)
        Note_Titles = ['Root/Octave', 'step', '2nd', '3rd (minor)', '3rd (Major)', '4th (Perfect)', 'Tritone',
                       '5th (Perfect)', '6th (Minor)', '6th (Major)', '7th (Minor)', '7th (Major)', 'Octave',
                       'Octave +']

        ## SETTINGS FOR PAUSE AND HOLD WHILE PLAYING NOTE
        NoteHold_Time = 1  # How long to hold each note -- just a default, likely overwritten by 'Timing' during 'Play_Notes'
        NoteHold_Phase_Rotation = np.pi / 6  # How much the differential phase moves during note (looks like rotating figure)
        NoteHold_Steps_Per_Second = 60  # How many steps to take as figure rotates (more steps looks like smoother rotation))
        Graph_Update_Interval_ms = 20  # How long the graph waits between updates, in milliseconds.

        ## SETTINGS FOR SOUND GENERATION
        Base_Freq = 440 / 4  # This frequency corresponds to our "Root" note -- 440 Hz is middle A.
        Sound_Block_Size = 4000  # How many sound samples are processed at a time. there are 44100 in a second.
        return

    def Establish_Sound(self):
        ## DESCRIPTION ##
        ## (No need to edit this function)
        ## This function initiates a connection to the speaker and establishes some useful variables.
        ## It starts a STREAM with the speaker, and the STREAM is assigned a CALLBACK FUNCTION.
        ## Any time the STREAM wants to send some more sound to the speaker, it calls the
        ## CALLBACK FUNCTION, which generates the sound data and saves it to the proper variable.

        # Declare global variables so they can be used in other functions without being passed as inputs
        global Stream
        global Sound_Start_Index
        global Sound_Sample_Rate
        global Base_Freq
        global Sound_Block_Size
        global StrikeTime
        global Sound_Save

        ## DEFINE PARAMETERS FOR LATER USE -- NO NEED TO EDIT
        Sound_Start_Index = 0
        Sound_Sample_Rate = 4400
        StrikeTime = 0
        Sound_Save = []

        ## INITIATE CONNECTION TO SPEAKER
        Stream = sd.OutputStream(samplerate=Sound_Sample_Rate, callback=self.Sound_Callback,
                                 blocksize=Sound_Block_Size)  # Define connection between code and speaker (ESPECIALLY IMPORTANT callback function provided for sound generation)
        Stream.start()  # Start sending data from code to speaker
        sd.wait()  # Don't terminate the sound until we say so

        return

    def Establish_Plot(self, Independent_Variable_Length):
        ## DESCRIPTION ##
        ## (No need to edit this function)
        ## This function creates the plotting window that shows the visualization of notes.
        ## It creates a figure, a line, and an ANIMATION.
        ## The ANIMATION repeatedly calls a CALLBACK FUNCTION.
        ## In this case, every time the callback function is called, the line's data is updated.

        # Declare global variables so they can be used in other functions without being passed as inputs
        global My_Line
        global Animation
        global fy_graph
        global fx_graph

        ## ESTABLISH PLOT -- THIS IS WHERE AXIS LIMITS ARE SET
        fx_graph = 1
        fy_graph = 1
        plt.ion()  # Turn on interactive mode
        Figure, ax = plt.subplots()  # Create figure and axes
        x = np.linspace(-1, 1,
                        Independent_Variable_Length)  # Create x coordinates for line -- will be changed every time callback is called.
        y = x  # Create y coordinates for line
        My_Line, = ax.plot(x, y, lw=2)  ## Plot the line, with data to be updated during animation.
        plt.show()  # display plot
        Animation = anim.FuncAnimation(fig=Figure, func=self.Plot_Callback, frames=None, fargs=[My_Line],
                                       interval=Graph_Update_Interval_ms)  # Create animation. Specify figure, callback function, and interval. "fargs" passes inputs to callback.
        My_Line._color = 0.9 * np.array([np.cos(2 * np.pi * (0 / 12 + 2 / 3)), np.cos(2 * np.pi * (0 / 12 + 1 / 3)),
                                         np.cos(
                                             2 * np.pi * (0 / 12 + 0 / 3))]) / 2 + 0.5  # Start line with pretty color.
        plt.pause(0.01)
        return

    def Sound_Callback(self, outdata, frames, time, status):

        ## DESCRIPTION ##
        ## (No need to edit this function)
        ## This function generates the sound that is sent to the speakers. It is assigned to
        ## the previously created STREAM, so that any time the STREAM calls this function
        ## any time it needs more sound data generated.

        global Sound_Start_Index
        # Establish time sequence
        t = (Sound_Start_Index + np.arange(frames)) / Sound_Sample_Rate

        # Create sound sinewaves
        Note1 = np.sin(2 * np.pi * t * Base_Freq * fx + Phase_Common)
        Note2 = np.sin(2 * np.pi * t * Base_Freq * fy + Phase_Common + Phase_Differential)
        Sound = Note1 / 3 + Note2
        # Fade volume over time
        Sound = np.multiply(Sound, np.exp(-((timepack.time() - StrikeTime + t - t[0]) / NoteHold_Time) ** 2))

        # Write Sound to stream's "outdata"
        outdata[:] = Sound.reshape(-1, 1)
        Sound_Save.extend(Sound.reshape(-1, 1))

        # Advance starting time for next sound block

        Sound_Start_Index += frames

    def Plot_Callback(self, frame, Line):
        ## DESCRIPTION ##
        ## (No need to edit this function)
        ## This function tells the animated graph what to draw.
        ## It is called every INTERVAL (usually less than a second) defined in the Establish_Plot function
        ## The crucial step is in the commands Line.set_xdata and Line.set_ydata

        Amplitude = np.exp(-((timepack.time() - StrikeTime) / NoteHold_Time) ** 2) ** (1 / 3)
        # HOUSEKEEPING -- establish time sequence and disharmony
        t = np.linspace(0, Line_Length, np.size(Line.get_xdata()))
        Disharmony_Mult = Disharmony / Line_Length / np.max([fy_graph, 0.1])

        ## LINEAR HARMONOGRAPH -- control x and y coordinates with sine waves of different frequencies
        X_Linear = np.sin(2 * np.pi * fx_graph * t + Phase_Common)  # Sinewave at frequency fx. Add common phase
        Y_Linear = np.sin(2 * np.pi * fy_graph * t * (1 + Disharmony_Mult) + Phase_Differential + Phase_Common)

        ## ROTARY HARMONOGRAPH -- control x and y coordinates with circles of different frequencies
        Circle1x = np.cos(2 * np.pi * fx_graph * t * (1 + Disharmony_Mult) + Phase_Common + Phase_Differential)
        Circle1y = np.sin(2 * np.pi * fx_graph * t * (1 + Disharmony_Mult) + Phase_Common + Phase_Differential)
        Circle2x = np.cos(2 * np.pi * fy_graph * t + Phase_Common)
        Circle2y = np.sin(2 * np.pi * fy_graph * t + Phase_Common)
        X_Rotary = (Circle1x - Circle2y) / 2
        Y_Rotary = (Circle1y - Circle2x) / 2

        ## ASSIGN DATA TO LINE (FEEL FREE TO PICK X/Y_LINEAR OR X/Y_ROTARY)
        Line.set_xdata(X_Linear * Amplitude)  # update the data
        Line.set_ydata(Y_Rotary * Amplitude)  # update the data
        plt.draw()  # Draw updated data

    def Play_Note(self, Note, Duration=1):
        ## DESCRIPTION
        ## This function controls the parameters that define the sound and graph.
        ## Although there are no direct calls to graph and sound generation in here,
        ## the variables that are changed do influence the graph and sound.

        # Establish global parameters so the edits here make changes in graph/sound callbacks
        global fx
        global fy
        global fy_graph
        global Phase_Differential
        global Phase_Common
        global StrikeTime
        global My_Line

        # Update note frequency and strike time
        fy = 2 ** (Note / 12)  # Change fy
        fy_graph = fy  # Update graph
        StrikeTime = timepack.time()  # Record time of striking this note
        # Add title
        plt.title(Note_Titles[int(np.log2(fy / fx) * 12.01) % 12])
        My_Line._color = 0.9 * np.array(
            [np.cos(2 * np.pi * (Note / 12 + 2 / 3)), np.cos(2 * np.pi * (Note / 12 + 1 / 3)),
             np.cos(2 * np.pi * (Note / 12 + 0 / 3))]) / 2 + 0.5
        plt.pause(1e-6)
        # Pause on this note
        NoteHold_Steps = int(NoteHold_Steps_Per_Second * Duration) + 1
        for NoteHold_Step in range(NoteHold_Steps):
            Phase_Differential += NoteHold_Phase_Rotation / NoteHold_Steps  # Add to phase difference between sinusoids
            plt.pause(1e-6)
            timepack.sleep(Duration / NoteHold_Steps)

    def Transition_Between_Notes(self, Note1, Note2, Transition_Time=0.1):
        ## DESCRIPTION
        ## This function controls the parameters that define the sound and graph.
        ## It only affects the graph, not the sound.
        ## Although there are no direct calls to graph and sound generation in here,
        ## the variables that are changed do influence the graph and sound.

        global Line_Length
        global My_Line
        global fy_graph
        # Initiate transition to next note
        Line_Length_Original = Line_Length
        Transition_Steps = int(Transition_Time * NoteHold_Steps_Per_Second) + 1
        Transition_Pause = Transition_Time / Transition_Steps
        for T in range(Transition_Steps):
            Quadratic_Shape_Fn = ((T - (Transition_Steps / 2)) / (
                        Transition_Steps / 2)) ** 2 + 0.01  # Shorten and regrow tail of figure during transition
            Note_Transition = (Note1 * (1 - (T + 1) / Transition_Steps) + Note2 * (T + 1) / Transition_Steps)
            Line_Length = Line_Length_Original * Quadratic_Shape_Fn
            My_Line._linewidth = 3 * Quadratic_Shape_Fn
            My_Line._color = Quadratic_Shape_Fn * 0.9 * np.array(
                [np.cos(2 * np.pi * (Note_Transition / 12 + 2 / 3)), np.cos(2 * np.pi * (Note_Transition / 12 + 1 / 3)),
                 np.cos(2 * np.pi * (Note_Transition / 12 + 0 / 3))]) / 2 + 0.5
            fy_graph = 2 ** (Note_Transition / 12)
            fy = fy_graph
            plt.pause(1e-6)
            timepack.sleep(Transition_Pause)
        Line_Length = Line_Length_Original  # Set figure back to full tail length again

    ## This takes the image and gets the average grayscale values across  squares of 64X64 pixels, ##
    ## gets the mean color of pixels for each row, and gets a sum of the normalized grayscale for  ##
    ## later turning this data into sine waves ##
    def Picture_To_RowInfo(self, Image):
        Image_Array = np.array(Image)
        YDim, XDim, NumChannels = Image_Array.shape
        Pixels_Per_Wave = 64
        Mean_Color = []
        Mean_GreyScale = []
        Phase_Advance = []
        Banded_GreyScale = np.zeros(XDim)

        for y in range(0, YDim, Pixels_Per_Wave):
            for x in range(0, XDim, Pixels_Per_Wave):
                Mean_Color.append(
                    [np.mean(Image_Array[y:y + Pixels_Per_Wave, x:x + Pixels_Per_Wave, RGB]) for RGB in range(3)])
                Mean_GreyScale.append(np.mean(Mean_Color))

            for x in range(XDim):
                Banded_GreyScale[x] = 1 - np.mean(
                    Image_Array[y:y + Pixels_Per_Wave, x, :]) / 255  # 0 to 1, 0 is light, 1 is dark
            Phase_Advance.append(np.cumsum(Banded_GreyScale))

        Mean_GreyScale = (Mean_GreyScale - np.min(Mean_GreyScale)) * 255 / (
                    np.max(Mean_GreyScale) - np.min(Mean_GreyScale))
        return Mean_Color, Mean_GreyScale, Phase_Advance

    ## This function turns the grayscale and color values into sine waves and gets their x,y coords for plotting ##
    def RowInfo_To_Waves(self, Image, Mean_GreyScale, Phase_Advance, LowFreq=1, HighFreq=100):
        Num_Waves = len(Phase_Advance)
        X_Dim, Y_Dim = Image.size
        X = np.linspace(0, X_Dim, X_Dim)
        X_Coords = []
        Y_Coords = []
        Y_Height = Y_Dim / Num_Waves

        for Row in range(Num_Waves):
            Freq = HighFreq - (HighFreq - LowFreq) * Mean_GreyScale[Row] / 255
            Wave = np.sin(2 * np.pi * Phase_Advance[Row] * (HighFreq - LowFreq) / X_Dim + LowFreq / X_Dim)
            X_Coords.append(X)
            Y_Coords.append(Wave * Y_Height / 2.1 + Y_Height * (Row + 0.5))
        return X_Coords, Y_Coords

    ## This plots the waves ##
    def Plot_Waves(self, X_Coords, Y_Coords, Mean_Color, Mean_GreyScale, Phase_Advance):
        for Wave in range(len(Phase_Advance)):
            plt.plot(X_Coords[Wave], Y_Coords[Wave], color=np.array(Mean_Color[Wave]) / 255, alpha=0.5,
                     linewidth=0.5 + 1.5 * (255 - Mean_GreyScale[Wave]) / 255)

    ## This connects to the computer speakers and plays the sound ##
    def Open_Stream(self):
        ## INITIATE CONNECTION TO SPEAKER
        Stream = sd.OutputStream(samplerate=44100, callback=self.Sound_Callback,
                                 blocksize=Block_Size)  # Define connection between code and speaker (ESPECIALLY IMPORTANT callback function provided for sound generation)
        Stream.start()  # Start sending data from code to speaker
        sd.wait()  # Don't terminate the sound until we say so

        ## DEFINE PARAMETERS FOR LATER USE -- NO NEED TO EDIT
        Sound_Start_Index = 0
        Sound_Sample_Rate = 44100
        Phase_Adjust = 0
        EndPhase = 0
        return Stream, Sound_Start_Index, Sound_Sample_Rate, Phase_Adjust, EndPhase

    def Sound_Function(self, Base_Freq, t, Phase_Adjust, SampleRate):
        Phase = 2 * np.pi * Base_Freq * Picture_Freq * t
        Sound = np.sin(Phase)
        return Sound, Phase



    # Create notes and timing array from a PIL image
    # Inputs: Image (recommended it is a compressed image)
    # Outputs: Notes and Timing array
    def Notes_Timing_from_Image(self, Image):
        img_array = np.array(Image)
        Raw_values = np.reshape(img_array, -1)
        Notes = Raw_values
        Timing = np.ones((len(Notes))) * 0.1

        for n in range(len(Raw_values)):
            Notes[n] = round(Raw_values[n] / 10)  # /21.25)
            Timing[n] = Raw_values[n] / 255

        return Notes, Timing

class Tree_Helpers:
    def __init__(self):
        self.Establish_Plot()

    def Establish_Plot(self):
        Figure, Axes = plt.subplots()
        Axes.set_facecolor([0, 0, 0])
        Axes.set_aspect('equal')
        plt.show(block=False)

    def Example(self):
        My_Tree = Tree()
        My_Trunk = Tree_Branch(BaseNode=Tree_Node(0, 0), Length=3, Heading=np.pi / 2)
        Branches = [My_Trunk]
        for n in range(5):
            Branches = My_Tree.Split_Group(Branches)

        Other_Trunk = Tree_Branch(BaseNode=Tree_Node(0, 0), Length=3, Heading=-np.pi / 2)
        Branches = [Other_Trunk]
        for n in range(5):
            Branches = My_Tree.Split_Group(Branches)

class Tree_Node:
    def __init__(self, X=0, Y=0):
        # DESCRIPTION: This function is called every time a node is instantiated.
        # A node just has an X and Y coordinate -- this is a simple class
        self.X = X
        self.Y = Y

class Tree_Branch:
    def __init__(self, Base_Input, Length_Input, Heading_Input):
        ## DESCRIPTION:
        ## This function runs every time a new Tree_Branch is instantiated.
        ## It assigns the properties Base, Length, and Heading.
        ## It should also call functions Grow_Tip_From_Base() and Draw()


        self.Base = Base_Input
        self.Length = Length_Input
        self.Heading = Heading_Input
        self.Tip = self.Grow_Tip_From_Base()
        self.Draw()

        ## FINISH EDITING ##

        return

    def Grow_Tip_From_Base(self):
        ## DESCRIPTION: Find/Return tip of branch, given its base, length, and heading.

        Tip = Tree_Node()
        Tip.X = self.Base.X + self.Length * np.cos(self.Heading)
        Tip.Y = self.Base.Y + self.Length * np.sin(self.Heading)
        return Tip

    def Draw(self):
        # DESCRIPTION: Draws branch onto existing plot

        plt.plot([self.Base.X, self.Tip.X], [self.Base.Y, self.Tip.Y], color=[0.4, 1, 0.4])
        plt.draw()

class Tree:
    def __init__(self):
        # DESCRIPTION:
        # This function is called when a Tree is instantiated.
        # It establishes some settings, but they can always be changed later.


        self.Branch_Angle = 60 * np.pi / 180
        self.Branches_Per_Split = 2
        self.Branch_Length = 1

    def Split_Branch(self, Parent_Branch):
        # DESCRIPTION:
        # Takes input of a Parent_Branch, and splits it into newly created Child Branches.
        # The base of each Child is marked as the tip of the Parent;
        # Each child's heading is calculated
        # And a new branch is created with the given Base, Length, Heading.


        Children = []
        for Branch_Counter in range(self.Branches_Per_Split):
            New_Heading = Parent_Branch.Heading + self.Branch_Angle * (
                        Branch_Counter - (self.Branches_Per_Split - 1) / 2)
            New_Branch = Tree_Branch(Base_Input=Parent_Branch.Tip, Length_Input=self.Branch_Length,
                                     Heading_Input=New_Heading)
            Children.append(New_Branch)
        return Children

    def Split_Group(self, Parents):
        # DESCRIPTION:
        # Takes input of a list of Parents, and splits each into newly created Child Branches.

        Group_Children = []
        for Parent_Branch in Parents:
            Children = self.Split_Branch(Parent_Branch)
            Group_Children.extend(Children)
        return Group_Children

class Turtle:
    def __init__(self):
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
        colors = cm.get_cmap(cm.viridis, 6)
        print(colors(0))

        # Call the turtle pen
        t = turtle.Pen()

        # set the background color
        turtle.bgcolor('black')

        for x in range(n):
            # Change the pen color
            t.pencolor((np.clip(colors(x), 2, 10) - 2) / 8.)

            # Change the pen line width based on n
            t.width(x // 100 + 1)

            # Move forward x amount
            t.forward(x)

            # Rotate 59 deg left
            t.left(59)

if __name__ == '__main__':
  pass

