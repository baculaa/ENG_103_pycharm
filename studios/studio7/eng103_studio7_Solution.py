import numpy as np
from matplotlib import pyplot as plt

class Node:
	def __init__(self, Xcoord = 0, Ycoord=0, Time=0, Value=0, Color = [1,0,0], Angle = 0):
		self.Xcoord = Xcoord
		self.Ycoord = Ycoord
		self.Time   = Time
		
		self.Value  = Value
		self.Color  = Color
		self.Angle  = Angle
		
		return

class Helpers:
	def __init__(self):
		return
	def Build_Plot(self, Num_Pixels_X, Num_Pixels_Y):
		## DESCRIPTION ##
		## This function establishes the plot figure and axes, to be used later on.
		plt.ion()
		[Fig, Ax] = plt.subplots()
		Ax.set_facecolor([0.1,0.1,0.2])
		plt.xlim([-1.1,1.1])
		plt.ylim([-1.1,1.1])
		plt.show(block=False) # Show plot, Do not halt code at this point
		return Fig, Ax
	def Draw_Frame(self, GrandList, Frame):
		## DESCRIPTION
		## This code draws points on the plot at a single frame
		## Color is according to each node's color property, defined in Build_Lists
		## Marker size is according to each node's Value property, also in Build_Lists
		Nx = len(GrandList)
		Ny = len(GrandList[0])
		Ax = plt.gca()	
		Ax.clear()
		for X in range(Nx):
			for Y in range(Ny):	
				My_Node = GrandList[X][Y][Frame]
				plt.plot(My_Node.Xcoord, My_Node.Ycoord, color = My_Node.Color,  marker=(5,1,np.arctan2(My_Node.Ycoord, My_Node.Xcoord)*180/np.pi - 90), markersize = 20*(My_Node.Value))	
				plt.draw()
		return
	def Draw_Sequence(self, GrandList, Duration):
		## DESCRIPTION 
		## This function plots each frame by calling Draw_Frame() and waits in between
		Num_Frames = len(GrandList[0][0])	
		for F in range(Num_Frames):
			self.Draw_Frame(GrandList, F)
			plt.title('Animation')
			plt.pause(Duration/Num_Frames)
		plt.title('Animation (End)')
		return

	def Control_Function_1(self, X, Y, T):
		## DESCRIPTION
		## This function defines the value property for any node, given its X coordinate, Y coordinate, and Time properties.
		Radius_Peak = (np.sin(2*np.pi* T * 2) +1.5)/2.5 # Radius from center that yields peak value (value=1 at peak)
		Radius_Width = 0.2 # Give a high value to nodes that are this CLOSE TO the peak radius 
		Angle_Peak = (2*np.pi* T * 2) # Angle from 0 that yields peak value (value=1 at peak)
		Direction_Peak = [np.cos(Angle_Peak), np.sin(Angle_Peak)] # This vector lies along the peak angle
		Angle_Width = 0.3 # Give a high value to nodes that are this CLOSE TO the peak angle 
		
		Radius = np.sqrt(X**2 + Y**2) #Define radius from center of this node
		Angle = np.arctan2(Y,X) #Define angle from 0 of this node
		Radius_Arg = (Radius-Radius_Peak)/Radius_Width #To be used in gaussian function
		Angle_Arg = (np.dot(Direction_Peak, [X,Y])/(Radius+1e-16) -1) / Angle_Width # to be used in gaussian function
		
		Output = np.exp(-Radius_Arg**2) * np.exp(-Angle_Arg**2) # The value given to the node.
		return Output
	def Control_Function_2(self, X, Y, T):
		## This function defines the value property for any node, given its X coordinate, Y coordinate, and Time properties.
		Output = (np.sin(2*np.pi*X) * np.cos(2*np.pi*Y) * np.sin(2*np.pi*T)+1)/2  # The value given to the node.
		return Output
	def Control_Function_3(self, X, Y, T):
		## This function defines the value property for any node, given its X coordinate, Y coordinate, and Time properties.
		Radius = np.sqrt(X**2 + Y**2)  #Define radius from center of this node
		Radius_Peak = (-np.cos(2*np.pi* T /1.5) +1)/1.5 # Radius from center that yields peak value (value=1 at peak)
		Radius_Width = 0.2  # Give a high value to nodes that are this CLOSE TO the peak radius 
		Radius_Arg = (Radius-Radius_Peak)/Radius_Width #To be used in gaussian function
		Output = np.exp(-Radius_Arg**2) # The value given to the node.
		return Output		
	def Build_Lists(self, Num_Pixels_X=10, Num_Pixels_Y=10, Num_Frames=20, Control_Func=Control_Function_1):
		## DESCRIPTION
		# This function builds a list of lists of lists of node objects.
		# The list's first index refers to the X position.
		# The list's second index refers to the Y position.
		# The list's third index refers to the Frame (The position in the animation time sequence). 
		List = [[[Node() for t in range(Num_Frames)] for y in range(Num_Pixels_Y)] for x in range(Num_Pixels_X)] #Establishes list of lists of lists of empty nodes.
		for X in range(Num_Pixels_X):
			for Y in range(Num_Pixels_Y):	
				for F in range(Num_Frames):
					List[X][Y][F].Xcoord = X/(Num_Pixels_X-1) *2-1 #Define x coordinate at this x index
					List[X][Y][F].Ycoord = Y/(Num_Pixels_Y-1) *2-1 #Define y coordinate at this y index
					List[X][Y][F].Frame  = F #Define frame
					List[X][Y][F].Time   = F/(Num_Frames-1) #Define time at this frame
					List[X][Y][F].Value  = Control_Func(List[X][Y][F].Xcoord, List[X][Y][F].Ycoord, List[X][Y][F].Time) # Use control function to assign value to this node. 
					List[X][Y][F].Color = [List[X][Y][F].Value, abs(np.sin(List[X][Y][F].Time/2*2*np.pi)), abs(np.sin((List[X][Y][F].Ycoord + List[X][Y][F].Ycoord)*2*np.pi))]			
		return List
	
class Studio_Functions:	
	def Find_Frame_With_MaxVal(self, GrandList, X_index, Y_index):
		### DESCRIPTION --- STUDIO PART 1 ####
		# This function takes inputs of the Grand List, and the X and Y indices of our point of interest.
		# We will find the frame at which this location shows a maximum value. 
		####################
		Num_Frames = len(GrandList[0][0])
		MaxVal   = 0
		MaxFrame = 0
		MaxNode  = GrandList[0][0][0]
		for Frame in range(Num_Frames):
			# In this loop, we're stepping through every frame in the animation.
			# We've already taken inputs defining the X and Y indices of our point of interest.
			# We want to find the Value of our point of interest at each of these frames.  
			# To do so, we'll have to properly index our GrandList	
			
			#------------------------------
			###### EDIT HERE (BEGIN) ######
			
			Current_Val = 0 # This line should be changed! 
			Current_Val = GrandList[X_index][Y_index][Frame].Value #REMOVE BEFORE PUBLISHING!
			# Set Current_Val to the value of the node at our inputs X_index and Y_index, and at this current Frame. 
			# It should say something like: 
			# Current_Val=GrandList[Index][Index][Index].Value
			
			###### EDIT HERE (END) ######
			#------------------------------
			
			if Current_Val > MaxVal: # If the value at this x,y, and frame is bigger than our previous maximum, we mark THIS value as the maximum, and THIS frame as the one containing the max value.
				MaxFrame = Frame     # Mark frame containing maximum value
				MaxVal = Current_Val # Mark maximum value
				MaxNode = GrandList[X_index][Y_index][Frame] # Mark Maximum Node
		return MaxFrame, MaxNode
	def Find_Value_vs_Time(self, GrandList, X_Index, Y_Index):
		### DESCRIPTION --- STUDIO PART 2 ####
		# This function takes inputs of the Grand List, and the X and Y indices of our point of interest.
		# We will return a list of all the Times, and another of all the Values corresponding to this location. 
		####################
		Num_Frames = len(GrandList[0][0])
		Times = []
		Values = []
		for Frame in range(Num_Frames):
			# In this loop, we're stepping through every frame in the animation.
			# We've already taken inputs defining the X and Y indices of our point of interest.
			# We want to find the value of our point of interest at each of these frames.  
			# To do so, we'll have to properly index our GrandList	
			#------------------------------
			###### EDIT HERE (BEGIN) ######
			Current_Time = 0 # CHANGE THIS LINE!
			Current_Val  = 0 # CHANGE THIS LINE!
			Current_Time = GrandList[X_Index][Y_Index][Frame].Time # REMOVE BEFORE PUBLISHING
			Current_Val  = GrandList[X_Index][Y_Index][Frame].Value # REMOVE BEFORE PUBLISHING
			#Set Current_Time to the node's Time property at this X_index,Y_index,and Frame.
			#Set Current_Val to the node's Value property at this X_index,Y_index,and Frame.			 
			###### EDIT HERE (END) ######
			#------------------------------
			
			Times.append(Current_Time)
			Values.append(Current_Val)
		return Times, Values
	def Find_Total_vs_Time(self, GrandList):
		### DESCRIPTION --- STUDIO PART 3 ####
		# This function takes an input of the Grand List
		# We will return a list of all the Times, and another of the total of node values at each frame
		####################	
		Nx = len(GrandList)
		Ny = len(GrandList[0])
		Num_Frames = len(GrandList[0][0])
		Totals = []
		Times = []
		for Frame in range(Num_Frames):
			Total=0
			for X in range(Nx):
				for Y in range(Ny):
					#------------------------------
					###### EDIT HERE (BEGIN) ######
					#Total  = 0 # CHANGE THIS LINE!
					Total += GrandList[X][Y][Frame].Value # REMOVE BEFORE PUBLISHING
					# ADD this node's value to the running Total.
					# The total should INCREASE by the value at this X, Y,and Frame.
					###### EDIT HERE (END) ######
					#------------------------------
			Totals.append(Total)
			Times.append(GrandList[0][0][Frame].Time)		
		return Times, Totals
	def Find_Brightest(self, GrandList):
		### DESCRIPTION --- STUDIO PART 4 ####
		# This function takes an input of the Grand List
		# We will return The very brightest node out of all locations and all times.
		####################		
		Nx 			  = len(GrandList)
		Ny 			  = len(GrandList[0])
		Num_Frames    = len(GrandList[0][0])
		Brightest_Val = 0
		Max_Brightness = 0
		for Frame in range(Num_Frames):
			for X in range(Nx):
				for Y in range(Ny):
					#------------------------------
					###### EDIT HERE (BEGIN) ######		
					Brightness = 0 #CHANGE THIS LINE!		
					# Brightness should be set equal to the average of RGB values defining this node's color.
					# For example, A color of [0.25, 0.50, 0.75] should have a brightness of 0.50	
					Brightness = sum(GrandList[X][Y][Frame].Color)/3 #DELETE BEFORE PUBLISHING!
					if Brightness > Max_Brightness:
						Max_Brightness = Brightness
						Brightest = Node() #CHANGE THIS LINE!
						Brightest = GrandList[X][Y][Frame] #DELETE BEFORE PUBLISHING!
						# Brightest should be set equal to the node at our current X, Y, and Frame.						
					###### EDIT HERE (END) ######
					#------------------------------						
		return Brightest


if __name__ == '__main__':
	## DESCRIPTION
	## This main function calls the other functions from Helpers and Studio_Functions
	## There is no need to edit this part, but you may change settings if you like
	
	# Initialize, define settings
	H = Helpers()
	Studio = Studio_Functions()
	Num_Pixels_X = 15 #Number of pixels to plot, X direction. Default 15
	Num_Pixels_Y = 15 #Number of pixels to plot, X direction. Default 15
	Num_Frames   = 80 #Number of frames to plot. Default 20
	Duration  	 = 1  #Duration of animation. Will likely take longer. Default 1
	X_Index_P1P2= 5 #Which node to track in part1 and part2
	Y_Index_P1P2= 12 #Which node to track in part1 and part2
	
	## DEFINE CONTROL FUNCTION that dictates values of nodes at every location/time
	Control_Func = H.Control_Function_3 # Function to control value of pixels
	
	# Build plot / lists and animate
	Fig, Ax   = H.Build_Plot(Num_Pixels_X, Num_Pixels_Y) #Establish plotting figure/axes
	GrandList = H.Build_Lists(Num_Pixels_X, Num_Pixels_Y, Num_Frames,  Control_Func) # Built List of nodes for every x,y,frame
	H.Draw_Sequence(GrandList, Duration) # Draw Animation (and wait between frames)
	plt.waitforbuttonpress()
	
	## PART 1: Find the frame with maximum value at a given X index / Y index. 
	MaxFrame, MaxNode = Studio.Find_Frame_With_MaxVal(GrandList, X_Index_P1P2, Y_Index_P1P2)
	H.Draw_Frame(GrandList, MaxFrame)
	plt.plot(MaxNode.Xcoord, MaxNode.Ycoord, color= [1,0.25,0.25], marker="o", markersize=40, fillstyle='none')
	plt.title('Part 1: Frame with Max Value at Given Location. Frame= %d' %MaxFrame)
	plt.waitforbuttonpress()
	
	## PART 2: Plot the value of one node value across time
	Times, Values = Studio.Find_Value_vs_Time(GrandList, X_Index_P1P2, Y_Index_P1P2)
	Ax.clear()
	plt.plot(Times, Values, color = [0.8,0.8,0.8])
	plt.plot(MaxNode.Time, MaxNode.Value, color= [1,0.25,0.25], marker="o", markersize=40, fillstyle='none')
	plt.draw()
	plt.title('Part 2: Value of Given Pixel Across Time')
	plt.waitforbuttonpress()
	
	## PART 3: Plot the total of all node values across time
	Times, Totals = Studio.Find_Total_vs_Time(GrandList)
	Ax.clear()
	plt.plot(Times, Totals, color=[0.8,0.8,0.8])
	plt.plot(Times[Totals.index(max(Totals))], Totals[Totals.index(max(Totals))], color= [1,0.25,0.25], marker="o", markersize=40, fillstyle='none')
	plt.draw()
	plt.title('Part 3: Total Value of All Pixels Across Time')
	plt.waitforbuttonpress()
	
	## PART 4: Find the Brightest Star
	Brightest = Studio.Find_Brightest(GrandList)
	Ax.clear()
	H.Draw_Frame(GrandList, Brightest.Frame)
	plt.title('Part 4: Find The Brightest Star')
	plt.plot(Brightest.Xcoord, Brightest.Ycoord, color= [1,0.25,0.25], marker="o", markersize=40, fillstyle='none')
	plt.draw()		
	plt.waitforbuttonpress()