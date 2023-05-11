import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import PIL


def Modify_Image_Array(Image):
	#######################################################
	############### DESCRIPTION ###########################
	# This function manipulates each pixel in an image
	#######################################################
	Image_Array = np.array(My_Image) #Convert to array so we can work with numbers
	XDim, YDim, NumChannels = Image_Array.shape #Measure size
	
	#Step through every pixel
	for x in range(XDim):
		for y in range(YDim):
			Image_Array[x,y,0] = (Image_Array[x,y,0])*x/XDim #Change R Channel
			Image_Array[x,y,1] = (Image_Array[x,y,1]/255)**(2)*255 #Change G Channel
			Image_Array[x,y,2] = Image_Array[x,y,2]*(1) #Change B Channel
			
	Modified = PIL.Image.fromarray(Image_Array) #Convert back from array to image
	#Modified = PIL.ImageOps.equalize(Modified) #Equalize channels
	plt.imshow(Modified) # Draw image onto plot
	plt.show() #Show plot
	return Modified
def Rotate_And_Paste(Canvas, Input, Angle, Location):
	
	Input = Input.convert('RGBA') ## Add alpha layer to image for use as mask
	Rotated = 	Input.rotate(Angle, expand=0, fillcolor = (0,0,0,0)) ## rotate image, fill extra space with transparent
	Canvas.paste(Rotated,(int(Location[0]), int(Location[1])),mask=Rotated) ## Paste rotated image using transparency as mask
	return Canvas

def Example_Rotate(Input):
	#######################################################
	############### DESCRIPTION ###########################
	# This function is a demonstration of rotating and pasting images
	# using functions from PIL directly.
	# The input image is manipulated and pasted onto a canvas several times.
	# Note that the canvas is larger than the input image.
	#######################################################
	
	#######################################################
	## Measure input image and make "Canvas" with 2x dimensions
	XDim, YDim = Input.size #Measure size of input image
	Canvas = PIL.Image.new(mode='RGB', size = [XDim*2, YDim*2]) #create "canvas" with 2x dimensions 
	# NOTE that you can change the size of the Canvas if you like.
	#######################################################
	#######################################################
	## Rotate and paste several copies of the input image.
	Rotated = Input.rotate(45) #Rotate 45 degrees
	Canvas.paste(Rotated,  (0,0)) #Paste result at location (0,0). 
	Input2 = Input.resize((int(XDim/8), int(YDim/8)))
	Canvas.paste(Input2.rotate(45*-1), (XDim,0)) #Rotate and paste all in one line. Paste at middle of top edge.
	Canvas.paste(Input2.rotate(45*-3),  (0,YDim)) #Rotate 135 degrees and paste at middle of left edge
	Canvas.paste(Input2.rotate(45*3), (XDim,YDim)) #Rotate and paste to location (XDim, YDim), center of canvas.
	
	Canvas.paste(Input2.rotate(90*3), (int(XDim/2),0)) #Rotate and paste
	Canvas.paste(Input2.rotate(90*0), (int(XDim),int(YDim/2))) #Rotate and paste
	Canvas.paste(Input2.rotate(90*1), (int(XDim/2),int(YDim))) #Rotate and paste
	Canvas.paste(Input2.rotate(90*2), (0,int(YDim/2))) #Rotate and paste


	#######################################################

	# Canvas = PIL.Image.blend(Canvas, Tiny, alpha=0.75)
	#######################################################
	## Overlay original image (transparent) on top of canvas -- just for fun
	Expanded = PIL.ImageOps.fit(Input, (XDim*2, YDim*2)) #Expand input to fit entire canvas
	Canvas = PIL.Image.blend(Canvas, Expanded, alpha=0.2) #Blend expanded input with the rest of the canvas
	#######################################################
	
	#######################################################
	## Display the results
	plt.imshow(Canvas) #Draw image in plot
	plt.show() #Show plot
	#######################################################
	return Canvas
def Example_Rotate_2(Input):
	#######################################################
	## DESCRIPTION ##
	# This is similar to "Example_Rotate" but it produces more fun results. 
	# This function is a demonstration of rotating and pasting images by calling another 
	# function within this script. It still uses PIL functions, but indirectly.
	# I wrote the function "Rotate_and_Paste" to eliminate those pesky black stripes on 
	# images rotated directly with PIL's "rotate".
	#######################################################
	
	#######################################################
	## Measure input image and make "Canvas" with 2x dimensions	
	XDim, YDim = Input.size
	CanvasScale = 2 # Define size of canvas relative to input
	Canvas = PIL.Image.new(mode='RGBA', size = [XDim*CanvasScale, YDim*CanvasScale], color=None)
	#######################################################

	#######################################################
	## Rotate and paste several copies of the input image.
	## NOTE that this uses the custom function "Rotate_And_Paste" rather than PIL. 
	Rotate_And_Paste(Canvas, Input, Angle=45*-6, Location=(XDim/2, 0))
	Rotate_And_Paste(Canvas, Input, Angle=45*-2, Location=(XDim, YDim/2))
	Rotate_And_Paste(Canvas, Input, Angle=45*-0, Location=(XDim/2, YDim))
	Rotate_And_Paste(Canvas, Input, Angle=45*-4, Location=(0, YDim/2))
	
	Rotate_And_Paste(Canvas, Input, Angle=45*-3, Location=(0, YDim))
	Rotate_And_Paste(Canvas, Input, Angle=45*-5, Location=(0, 0))
	Rotate_And_Paste(Canvas, Input, Angle=45*-7, Location=(XDim, YDim))
	Rotate_And_Paste(Canvas, Input, Angle=45*-1, Location=(XDim, 0))
	
	
	#######################################################

	#######################################################
	## Display the results
	plt.imshow(Canvas)
	plt.show()
	#######################################################

	return(Canvas)
def Example_Mirror(Input):
	#######################################################
	## DESCRIPTION ##
	# This demonstrates using PIL.ImageOps.mirror (and flip).
	# Note that it is PIL.ImageOps.x rather than PIL.Image.x
	# The input image is manipulated and pasted onto a canvas several times.
	# Note that the canvas is larger than the input image.
	#######################################################
	
	#######################################################
	## Measure input image and make "Canvas" with 2x dimensions		
	XDim, YDim = Input.size
	Canvas = PIL.Image.new(mode='RGB', size = [XDim*2, YDim*2])
	#######################################################

	#######################################################
	## Place input and flipped/rotated input on Canvas.	
	Canvas.paste((Input), (0,0))
	Canvas.paste(PIL.ImageOps.flip(Input), (XDim,0))
	Canvas.paste(PIL.ImageOps.mirror(Input), (0,YDim))
	Canvas.paste(PIL.ImageOps.mirror(PIL.ImageOps.flip(Input)), (XDim,YDim))	
	#######################################################

	#######################################################
	## Display the results	
	plt.imshow(Canvas)
	plt.show()
	#######################################################
	return Canvas
def Example_All_Transforms(My_Input_Image):

	## Example Rotation
	Rotated = My_Input_Image.rotate(45)
	#Plot
	plt.imshow(Rotated)
	plt.title('Rotated')
	plt.show()
	
	## Example Flip (Vertical)
	Flipped = PIL.ImageOps.flip(My_Input_Image)
	#Plot
	plt.imshow(Flipped)
	plt.title('Flipped')
	plt.show()
	
	## Example Mirror (Horizontal)
	Mirrored = PIL.ImageOps.mirror(My_Input_Image)
	#Plot
	plt.imshow(Mirrored)
	plt.title('Mirrored')
	plt.show()
	
	## Example Paste
	XDim, YDim = My_Input_Image.size #Measure input size
	Canvas = PIL.Image.new(mode='RGBA', size = [XDim*3, YDim*3], color=None) #Make Canvas 3x size
	Canvas.paste(My_Input_Image, (int(XDim/2), int(YDim/2))) #Paste input image onto newly created canvas
	#Plot
	plt.imshow(Canvas)
	plt.title('Pasted')
	plt.show()
	
	## Example Multiple Transforms
	Canvas.paste(PIL.ImageOps.flip(PIL.ImageOps.mirror( My_Input_Image.rotate(20) )), (int(XDim*1.8), int(YDim*1.9)) )
	#Plot
	plt.imshow(Canvas)
	plt.title('Several Transforms')
	plt.show()	
		
if __name__ == '__main__':

	#######################################################
	## Define FileName -- The name of a file IN THE SAME FOLDER as this script.
	FileName = 'borbor.jpg'
	
	## Open Image, display/save results.
	My_Image = PIL.Image.open(FileName) #Open image file into memory (doesn't display the picture)
	plt.imshow(My_Image) # Draw image onto plot
	plt.show() #Show plot
	#######################################################
	
	#######################################################
	## Examples -- Uncomment these examples so that they run and show what sort of things 
	# are possible. To see the code that produces those transforms, take a look at the
	# corresponding function above. Copy and paste as needed to make your own!
	
	# Example_All_Transforms(My_Image)
	Example_Rotate(My_Image) #uncomment me to see a rotation!
	#Example_Rotate_2(My_Image) #uncomment to see another rotation! (With no black space)
	#Example_Mirror(My_Image) #uncomment me to see a flip/mirror!
	#Modified = Modify_Image_Array(My_Image) #This is an example of modifying pixel values
	#######################################################

	#######################################################
	## EDIT HERE ##
	## Write some code here, or simply modify what you find in the given functions.
	#######################################################
