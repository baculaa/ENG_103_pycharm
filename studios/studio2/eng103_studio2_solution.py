import numpy as np
from matplotlib import pyplot as plt


def Plot_Paintings(Wall_Length, Painting_Length, Num_Paintings, Wall_Height, Painting_Height):
	#________________________________
	##  FUNCTION DESCRIPTION   ##
	## This function plots the arrangement of paintings on a wall.
	## Inputs: Wall length/height, painting length/height, number of paintings
	## Outputs: Plot of wall (No values returned)
	#________________________________
	
	
	#________________________________
	##   HOUSEKEEPING FOR PLOTS   ##
	plt.ion() #Turn on interactive mode -- this way your plot updates when you add new things
	plt.xlim([-0.2*Wall_Length, 1.2*Wall_Length])
	plt.ylim([-0.5*Wall_Height, 1.5*Wall_Height])
	plt.gca().set_aspect(1) #Keep aspect ratio equal (don't stretch the plot)
	Plot_StickFigure()
	#________________________________
	
	
	#________________________________	
	##   PLOT THE WALL ITSELF   ##
	##   ! USE THIS ! as a reference when you write your code below
	Wall_Corners = Find_Corners(Center_X = Wall_Length/2, Center_Y = Wall_Height/2, Span_X = Wall_Length, Span_Y = Wall_Height) #Find corners using call to function "Find_Corners"
	plt.plot(Wall_Corners[:,0], Wall_Corners[:,1], linewidth=2, color='black')   ## Plot the wall (as lines connecting its corners)
	plt.fill(Wall_Corners[:,0], Wall_Corners[:,1], color='lightcyan') ## Fill the wall with color
	plt.waitforbuttonpress()   ## Display the plot and wait until a button is pressed before continuing
	#________________________________
			
			
	#________________________________		
	##   CALCLUATE SPACING BETWEEN PAINTINGS   ##
	
	###################################################
	###### SOLUTION !!!  DELETE BEFORE PUBLISHING #####
	Painting_req_space = Painting_Length*Num_Paintings

	if Painting_req_space >= Wall_Length:
		print("Oh no bad your paintings wont fit")
	else:
		print("Yay they fit")

	Spacing = (Wall_Length-(Painting_Length*Num_Paintings))/(Num_Paintings+1) ## Calculate Spacing between paintings
	##########################
	
	##########################
	###### EDIT HERE !!! #####
	#Spacing = [ __WRITE__YOUR__SPACING__EXPRESSION__HERE__ ]  # Calculate spacing between paintings
	##########################
	#________________________________
	
	
	#________________________________
	##   PLOT EACH PAINTING IN FOR LOOP  ##
	for Painting in range(Num_Paintings):
		
		###################################################
		###### SOLUTION !!!  DELETE BEFORE PUBLISHING #####
		X_Position = Spacing*(Painting+1) + Painting_Length*(1/2+Painting) ## Calculate X coordinate marking center of painting
		Corners = Find_Corners(Center_X = X_Position, Center_Y = Wall_Height/2, Span_X = Painting_Length, Span_Y = Painting_Height) ## Find corners using call to function "Find Corners"
		plt.plot(Corners[:,0], Corners[:,1], color='black') ## Plot the corners in the defined order (the order has already been defined outside of the loop)
		# Color = np.array([np.cos(2*np.pi*-Painting/(Num_Paintings*1.2)),np.cos(2*np.pi*(-Painting/(Num_Paintings*1.2) +1/3)),np.cos(2*np.pi*(-Painting/(Num_Paintings*1.1) +2/3))])/2+0.5
		plt.fill(Corners[:, 0], Corners[:, 1], color='blue')
		plt.waitforbuttonpress() ## Display the plot and wait until a button is pressed before continuing
		###################################################
		
		###### EDIT HERE !!! #####
		#X_Position =  __WRITE__YOUR__CENTER__POSITION__CALCULATION__HERE__  ## Calculate X coordinate marking center of painting. This one you have to write from scratch.
		#Corners =   __WRITE__YOUR__CALL__TO__"Find_Corners"__HERE__   ## Find corners using call to function "Find Corners". Refer to previous call for inspiration.
		#plt.plot(__WRITE__YOUR__CALL__TO__"plt.plot"__HERE__)         ## Plot the frame / outline of each. Refer to previous call for inspiration.
		#plt.fill(__WRITE__YOUR__CALL__TO__"plt.fill"__HERE__)		   ## Fill each fram with color. Refer to previous call for inspiration.
		#plt.waitforbuttonpress() ## Just uncomment this line so that your plot waits for your input to move forward.
		##########################
	#________________________________	
	
def Plot_StickFigure(Offset = [-1.3,0]):
	#________________________________
	##   DESCRIPTION   ##
	## No need to edit this function
	## This plots a stick figure to stare at your wall full of art
	#________________________________
	Vertices =  np.array([[-0.05443548,  0.49188312],
				 [-0.10685484,  0.47294372],
				 [-0.18548387,  0.52705628],
				 [-0.22782258,  0.71103896],
				 [-0.18951613,  0.84361472],
				 [-0.07459677,  0.91125541],
				 [ 0.09677419,  0.92478355],
				 [ 0.13508065,  0.82467532],
				 [ 0.125     ,  0.5974026 ],
				 [ 0.08669355,  0.47835498],
				 [ 0.01209677,  0.4702381 ],
				 [-0.02620968,  0.49458874],
				 [-0.02419355,  0.14015152],
				 [ 0.34072581, -0.08170996],
				 [-0.03024194,  0.14285714],
				 [-0.41935484,  0.10497835],
				 [-0.02217742,  0.14015152],
				 [-0.01008065, -0.38744589],
				 [ 0.25806452, -0.77435065],
				 [ 0.43951613, -0.7797619 ],
				 [ 0.26209677, -0.7797619 ],
				 [-0.01209677, -0.3982684 ],
				 [-0.01209677, -0.39556277],
				 [-0.23790323, -0.76623377],
				 [-0.45766129, -0.75811688]])
	plt.plot(Vertices[:,0]+Offset[0], Vertices[:,1]+Offset[1])		
def Find_Corners(Center_X, Center_Y, Span_X, Span_Y):
	#________________________________
	##   DESCRIPTION   ##
	## No need to edit this function
	## This returns the corners of a rectangle for which the center and span are provided. 
	## Inputs: Center of rectangle (X and Y) and dimensions/span (X and Y).
	## Outputs: Corners of rectangle as array
	#________________________________
	
	Upper_Left  = (Center_X - Span_X/2, Center_Y + Span_Y/2)
	Upper_Right = (Center_X + Span_X/2, Center_Y + Span_Y/2)
	Lower_Left = (Center_X - Span_X/2, Center_Y - Span_Y/2)
	Lower_Right= (Center_X + Span_X/2, Center_Y - Span_Y/2) 
	Corners = [Upper_Left, Upper_Right, Lower_Right, Lower_Left, Upper_Left]			
	return np.array(Corners)

if __name__ == '__main__':
	Plot_Paintings(Wall_Length = 10, Painting_Length = 2.5, Num_Paintings = 3 , Wall_Height = 5, Painting_Height = 3)


