import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import PIL



def Import_Image(FileName):
	My_Image = PIL.Image.open(FileName)
	return My_Image#.resize((256,256))

def Modify_Image_Array(Image):
	Image_Array = np.array(My_Image)
	XDim, YDim, NumChannels = Image_Array.shape
	for x in range(XDim):
		Image_Array[x,:,2] = Image_Array[x,:,2]**(1/3)
	Modified = PIL.Image.fromarray(Image_Array)
	Modified = PIL.ImageOps.equalize(Modified)
	return Modified

def Rotate_And_Paste(Canvas, Input, Angle, Location):
	Rotated = 	Input.rotate(Angle, expand=0, fillcolor = (0,0,0,0))
	Canvas.paste(Rotated,(int(Location[0]), int(Location[1])),Rotated)
	return Canvas


# Canvas.paste(Input.rotate(90*0), (int(XDim/2),0))
# Canvas.paste(Input.rotate(90*1), (0,int(YDim/2)))
# Canvas.paste(Input.rotate(90*2), (int(XDim/2),int(YDim)))
# Canvas.paste(Input.rotate(90*3), (int(XDim),int(YDim/2)))

# Center = PIL.ImageOps.fit(Input, (XDim*2, YDim*2))
# Blended = PIL.Image.blend(Canvas, Center,0.0)
# Canvas.paste(Blended.rotate(0), (0,0))
def Composite_Image(Input):
	print(Input.size)
	XDim, YDim = Input.size
	Canvas = PIL.Image.new(mode='RGB', size = [XDim, YDim*4])
	
	Canvas.paste(Input.rotate(0), (0,0))
	Canvas.paste(PIL.ImageOps.flip(Input.rotate(0)), (0,YDim))
	Canvas.paste(Input.rotate(0), (0,YDim*2))
	Canvas.paste(PIL.ImageOps.flip(Input.rotate(0)), (0,YDim*3))

	plt.imshow(Canvas)
	plt.show()
def Composite_Image2(Input):

	Input = Input.convert('RGBA')
	XDim, YDim = Input.size
	CanvasScale = 2
	Canvas = PIL.Image.new(mode='RGBA', size = [XDim*CanvasScale, YDim*CanvasScale], color=None)

	Rotate_And_Paste(Canvas, Input, Angle=45*-0, Location=(XDim/2, 0))
	Rotate_And_Paste(Canvas, Input, Angle=45*-4, Location=(XDim/2, YDim))	
	Rotate_And_Paste(Canvas, Input, Angle=45*-6, Location=(0, YDim/2))
	Rotate_And_Paste(Canvas, Input, Angle=45*-2, Location=(XDim, YDim/2))

	Rotate_And_Paste(Canvas, Input, Angle=45*-7, Location=(0, 0))
	Rotate_And_Paste(Canvas, Input, Angle=45*-5, Location=(0, YDim))
	Rotate_And_Paste(Canvas, Input, Angle=45*-3, Location=(XDim, YDim))
	Rotate_And_Paste(Canvas, Input, Angle=45*-1, Location=(XDim, 0))

	plt.imshow(Canvas)
	plt.show()
	return(Canvas)

def Example_Transforms(My_Input_Image):

	Rotated = My_Input_Image.rotate(45)
	plt.imshow(Rotated)
	plt.title('Rotated')
	plt.show()
	
	Flipped = PIL.ImageOps.flip(My_Input_Image)
	plt.imshow(Flipped)
	plt.title('Flipped')
	plt.show()
	
	Mirrored = PIL.ImageOps.mirror(My_Input_Image)
	plt.imshow(Mirrored)
	plt.title('Mirrored')
	plt.show()
	
	XDim, YDim = My_Input_Image.size
	Canvas = PIL.Image.new(mode='RGBA', size = [XDim*3, YDim*3], color=None)
	Canvas.paste(My_Input_Image, (int(XDim/2), int(YDim/2)))
	plt.imshow(Canvas)
	plt.title('Pasted')
	plt.show()
	Canvas.paste(PIL.ImageOps.flip(PIL.ImageOps.mirror(My_Input_Image.rotate(20))), (int(XDim*1.8), int(YDim*1.9)) )
	plt.imshow(Canvas)
	#plt.imshow(Canvas.paste(PIL.ImageOps.flip(PIL.ImageOps.mirror(Input_Image.rotate(20))), (int(XDim/3), int(YDim)) ))
	plt.title('Several Transforms')
	plt.show()
	
	
if __name__ == '__main__':
	
	FileName = 'bean.jpg'
	
	My_Image = Import_Image(FileName)
	plt.imshow(My_Image)
	plt.show()
	
	# My_Image.save('Saved_Output.jpg')
	
	# Example_Transforms(My_Image)
	
	Modified = Modify_Image_Array(My_Image)
	Reflected = Composite_Image(Modified)
	#Composite_Image2(Reflected)
	
	