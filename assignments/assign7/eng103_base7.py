## AUTHOR: Alexandra Bacula
## ENG 103 base code 7


import numpy as np
import matplotlib.pyplot as plt
import PIL

class image_manipulation:

    def Import_Image(self, FileName):
        My_Image = PIL.Image.open(FileName)
        return My_Image  # .resize((256,256))


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

                #####################
                ##### EDIT HERE #####
                #####################

                # Save the pixel value of the original image to the opposite X value in the Flipped_Image_Array
                ## ie, you want the lowest x index in the original image to become the highest x index in the flipped image
                ## You will need to have after that operation  -1 because the python indexes at 0 not 1
                ## The y index will be the same

                # The Image_Array is indexed as follows: Image_Array[x,y,:]
                ### The colon is there bcause there are three values in that last spot (RGB)
                ####The color lets you save all three at once

                # You will end up with Flipped_Image_Array[something -1,y,:] = Image_Array[x,y,:]

                print("Flipping Image")

                #############################
                ##### STOP EDITING HERE #####
                #############################

        # This converts your array back into an image with the correct value type
        Flipped_Image = PIL.Image.fromarray((Flipped_Image_Array).astype(np.uint8))

        # Return the flipped image
        return Flipped_Image


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
                #####################
                ##### EDIT HERE #####
                #####################

                # Save the R,G,and B pixel value of the original image to 255-original value in the Combined_Image_Array
                ## ie, you will end up with three lines specifying each new R, G, B value
                ## The x and y index will be the same

                # The Image_Array is indexed as follows:
                ### Image_Array[x,y,0] is R
                ### Image_Array[x,y,1] is G
                ### Image_Array[x,y,2] is B
                ### The colon is there bcause there are three values in that last spot (RGB)
                ####The color lets you save all three at once

                print("Inverting Color")

                #############################
                ##### STOP EDITING HERE #####
                #############################

    def Combine_Images(self,Image1,Image2):
        ##########################################
        ## MAKE SURE BOTH ARE COLOR IMAGES!!!!! ##
        ##########################################

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
        Combined_Image_Array = np.zeros((XDim,YDim,3))

        # Go through each pixel in X and Y
        for x in range(XDim):
            for y in range(YDim):

                #####################
                ##### EDIT HERE #####
                #####################

                # Write If Statements to alternate which image you save a pixel value from to the combined image array
                ## ie, do something like every even x value save pixel from Image1, and every odd x value save pixel from Image2
                ### you could also do this with the y dimension instead
                ### or try it with both!
                ### or you can pick some other condition, play around and see what conditions you like best!

                # The all image arrays are indexed as follows: Image_Array[x,y,:]
                ### The colon is there bcause there are three values in that last spot (RGB)
                ####The color lets you save all three at once
                #### MAKE SURE BOTH OF YOUR INPUT IMAGES ARE COLOR!!!!

                print('Combining Images')

                #############################
                ##### STOP EDITING HERE #####
                #############################

        # This converts your array back into an image with the correct value type
        Combined_Image = PIL.Image.fromarray((Combined_Image_Array).astype(np.uint8))

        # Return the flipped image
        return Combined_Image

    #####################
    ##### EDIT HERE #####
    #####################

    # Write your own custom manipulation function

    # HELPFUL INFO:

    ## Indexing a color image:
    ### Image[x,y,:] is all the RGB values for one pixel
    ### Image[x,y,0] is the R value for one pixel
    ### Image[x,y,1] is the G value for one pixel
    ### Image[x,y,2] is the B value for one pixel

    ## Image Dimensions:
    ## Image.shape[0] is the x dimension
    ## Image.shape[1] is the y dimension
    ## Image.shape[2] is the pixel value dimension (3 for color, 1 for gray)

    #############################
    ##### STOP EDITING HERE #####
    #############################

if __name__ == '__main__':

    # Create an instance of the image_manipulation class
    image_manip = image_manipulation()

    ###################
    #### EDIT HERE ####
    ###################
    # Import your image (make sure it is in your current directory, or specify the path)
    My_Image = image_manip.Import_Image('runt.jpg')
    My_Image2 = image_manip.Import_Image('marble.jpg')
    ###########################
    #### STOP EDITING HERE ####
    ###########################


    # Call the Flip image function
    Flipped_Image = image_manip.Flip_Image(My_Image)

    # Call the Invert Color Function
    Invert_Color_Image = image_manip.Invert_Color(My_Image)

    # Call the Combined image function
    Combined_Image = image_manip.Combine_Images(My_Image,My_Image2)

    ###################
    #### EDIT HERE ####
    ###################

    # Call your custom function here!

    ###########################
    #### STOP EDITING HERE ####
    ###########################

    # Show the original image
    plt.imshow(My_Image)
    # Wait until the image is closed to continue
    plt.waitforbuttonpress()


    # Show the flipped image
    plt.imshow(Flipped_Image)
    # Wait until the image is closed to continue
    plt.waitforbuttonpress()


    # Show the inverted color image
    plt.imshow(Invert_Color_Image)
    # Wait until the image is closed to continue
    plt.waitforbuttonpress()


    # Show the combined image
    plt.imshow(Combined_Image)
    # Wait until the image is closed to continue
    plt.waitforbuttonpress()

    ###################
    #### EDIT HERE ####
    ###################

    # Show the results of your custom function

    ###########################
    #### STOP EDITING HERE ####
    ###########################
