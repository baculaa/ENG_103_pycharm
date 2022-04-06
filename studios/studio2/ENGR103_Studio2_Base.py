import numpy as np
from matplotlib import pyplot as plt


def Plot_Paintings(Wall_Length=20, Painting_Length=0.5, Num_Paintings=6, Wall_Height=2, Painting_Height=1):
	#________________________________
	##   DESCRIPTION   ##
	## This function plots the arrangement of paintings on a wall.
	## Inputs: Wall length/height, painting length/height, number of paintings
	## Outputs: Plot of wall (No values returned)
	#________________________________
	
	
	#________________________________
	##   HOUSEKEEPING FOR PLOTS   ##
	plt.ion() #Turn on interactive mode
	plt.gca().set_aspect(1) #Keep aspect ratio equal (don't stretch the plot)
	#________________________________
	
	
	#________________________________	
	##   PLOT THE WALL ITSELF   ##
	Wall_Corners = Find_Corners(Center_X = Wall_Length/2, Center_Y = Wall_Height/2, Dim_X = Wall_Length, Dim_Y = Wall_Height) #Find corners using call to function "Find_Corners"
	Order  = [0,1,2,3,0]   ## Define order in which to plot these points. We will draw from the first point to the second, third, fourth, and then back to the first to complete the path
	plt.plot(Wall_Corners[Order,0], Wall_Corners[Order,1])   ## Plot the corners in the defined order
	plt.waitforbuttonpress()   ## Display the plot and wait until a button is pressed before continuing
	#________________________________
			
			
	#________________________________		
	##   CALCLUATE SPACING BETWEEN PAINTINGS   ##
	
	###################################################
	###### SOLUTION !!!  DELETE BEFORE PUBLISHING #####
	Spacing = (Wall_Length-(Painting_Length*Num_Paintings))/(Num_Paintings+1) ## Calculate Spacing between paintings
	##########################
	
	##########################
	###### EDIT HERE !!! #####
	## Calculate spacing between paintings
	##########################
	#________________________________
	
	
	#________________________________
	##   PLOT EACH PAINTING IN FOR LOOP  ##
	for Painting in range(Num_Paintings):
		
		###################################################
		###### SOLUTION !!!  DELETE BEFORE PUBLISHING #####
		X_Position = Spacing*(Painting+1) + Painting_Length*(1/2+Painting) ## Calculate X coordinate marking center of painting
		Corners = Find_Corners(Center_X = X_Position, Center_Y = Wall_Height/2, Dim_X = Painting_Length, Dim_Y = Painting_Height) ## Find corners using call to function "Find Corners"
		plt.plot(Corners[Order,0], Corners[Order,1]) ## Plot the corners in the defined order (the order has already been defined outside of the loop)
		plt.waitforbuttonpress() ## Display the plot and wait until a button is pressed before continuing
		###################################################
		
		###### EDIT HERE !!! #####
		## Calculate X coordinate marking center of painting
		## Find corners using call to function "Find Corners"
		## Plot the corners in the defined order (the order has already been defined outside of the loop)
		## Display the plot and wait until a button is pressed before continuing
		##########################
	#________________________________	
	
	
def Find_Corners(Center_X, Center_Y, Dim_X, Dim_Y):
	#________________________________
	##   DESCRIPTION   ##
	## No need to edit this function
	## This returns the corners of a rectangle for which the center and span are provided. 
	## Inputs: Center of rectangle (X and Y) and dimensions (X and Y). "Dim" is short for "Dimension"
	## Outputs: Corners of rectangle as array
	#________________________________
	
	UpLeft  = (Center_X - Dim_X/2, Center_Y + Dim_Y/2)
	UpRight = (Center_X + Dim_X/2, Center_Y + Dim_Y/2)
	LowLeft = (Center_X - Dim_X/2, Center_Y - Dim_Y/2)
	LowRight= (Center_X + Dim_X/2, Center_Y - Dim_Y/2) 
	Corners = [UpLeft, UpRight, LowRight, LowLeft]			
	return np.array(Corners)


if __name__ == '__main__':
	Plot_Paintings(Wall_Length = 20, Painting_Length = 0.5, Num_Paintings = 6 )


