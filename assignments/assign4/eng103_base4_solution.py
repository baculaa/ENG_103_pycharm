## AUTHOR: Alexandra Bacula and Carson Rivard
## ENG 103 base code 4


import numpy as np
import matplotlib.pyplot as plt
import PIL
import sounddevice as sd
import time
import wavio

Base_Freq = 50
Block_Size = 2000
Picture_Freq = 0
global Sound_Save
Sound_Save = []

class sound_and_sine:

    #######################################################
    ####### DO NOT CHANGE ANYTHING IN THIS CLASS!!! #######
    #######################################################


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

        Mean_GreyScale = (Mean_GreyScale - np.min(Mean_GreyScale)) * 255 / (np.max(Mean_GreyScale) - np.min(Mean_GreyScale))
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

    def Sound_Callback(self, outdata, frames, time,
                       status):  # This function definition line MUST appear just like this to be a valid callback
        # DECLARE GLOBAL VARIABLES -- necessary because we don't decide when this callback is called or what variables are input to it.
        ## This function is called when the speaker wants more sound data to play.
        ## No need to edit here, unless you want to define a different sound generating function ("Sound_Function")
        ## Care is taken to match the phase at the end of one block to that =at the beginning of the next block.

        ## DEFINE THESE VARIABLES AS GLOBAL SO THAT OUR EDITS SHOW UP IN CALLBACK FUNCTIONS FOR GRAPH/SOUND
        global Sound_Start_Index
        global EndPhase
        global Phase_Adjust


        ## SPECIFY FUNCTION THAT GENERATES SOUND (SHOULD OUTPUT SOUNDWAVE AND PHASE)
        Sound_Function = self.Sound_Function

        # ESTABLISH TIME SEQUENCE FOR THIS BLOCK
        t = (Sound_Start_Index + np.arange(frames + 1)) / Sound_Sample_Rate
        # t = t.reshape(-1, 1)

        # ADJUST FOR PHASE MISMATCH FROM LAST BLOCK
        [Blank, BeginPhase] = Sound_Function(Base_Freq, np.array([t[0]]), Phase_Adjust=0, SampleRate=Sound_Sample_Rate)
        Phase_Adjust = EndPhase - BeginPhase

        # WRITE OUTPUT TO SPEAKER
        [Sound, Phase] = Sound_Function(Base_Freq, t[0:-1], Phase_Adjust=0, SampleRate=Sound_Sample_Rate)
        outdata[:] = Sound.reshape(-1, 1)

        # MARK ENDING PHASE AND INDEX FOR USE IN NEXT BLOCK
        EndPhase = Phase[-1]
        Sound_Start_Index += frames

        # Write Sound to stream's "outdata"
        outdata[:] = Sound.reshape(-1, 1)
        Sound_Save.extend(Sound.reshape(-1, 1))

    def Sound_Function(self, Base_Freq, t, Phase_Adjust, SampleRate):
        Phase = 2 * np.pi * Base_Freq * Picture_Freq * t
        Sound = np.sin(Phase)
        return Sound, Phase



class image_manipulation:

    def Import_Image(self, FileName):
        My_Image = PIL.Image.open(FileName)
        return My_Image  # .resize((256,256))

    def Gray_Image(selfself, Image):
        Gray_Image = Image.convert("LA")
        return Gray_Image

    def Compress_Image(self, Image, avg_factor):

        Gray_Array = np.array(self.Gray_Image(Image))
        Color_Array = np.array(Image)

        color_values = Color_Array[:,:,0:3]
        print(color_values.shape)
        gray_values = Gray_Array[:, :, 0]
        XDim, YDim = gray_values.shape
        x_avg = int(XDim / avg_factor)
        y_avg = int(YDim / avg_factor)
        gray_avg = np.zeros((x_avg, y_avg))
        color_avg = np.zeros((x_avg, y_avg))

        for x in range(x_avg):
            for y in range(y_avg):
                orig_x_index = x * avg_factor
                orig_y_index = y * avg_factor
                avg_value = np.reshape(gray_values[orig_x_index:orig_x_index + avg_factor,
                                       orig_y_index:orig_y_index + avg_factor], -1)
                gray_avg[x, y] = np.average(avg_value)

                avg_value_c = np.reshape(color_values[orig_x_index:orig_x_index + avg_factor,
                                       orig_y_index:orig_y_index + avg_factor,0:3], -1)
                print(avg_value_c)
                color_avg[x,y] = np.average(avg_value_c)

        return gray_avg,color_avg

    def Notes_Timing_from_Image(self, Image, avg_factor):
        img_array,color_avg = np.array(self.Compress_Image(Image, avg_factor))
        Raw_values = np.reshape(img_array, -1)
        Raw_color = np.reshape(color_avg,-1)
        Notes = Raw_values
        Timing = np.ones((len(Notes))) * 0.1

        for n in range(len(Raw_values)):
            Notes[n] = round(Raw_values[n] / 10)  # /21.25)
            Timing[n] = Raw_color[n] / 255
        print(Timing)
        print(Notes)
        return Notes, Timing


if __name__ == '__main__':

    sound_and_sine = sound_and_sine()
    image_manip = image_manipulation()

    Blank = image_manip.Import_Image('Blank.jpg')
    My_Image = image_manip.Import_Image('borbor.jpg')

    # NumWaves = 100
    #
    # Mean_Color, Mean_GreyScale, Phase_Advance = sound_and_sine.Picture_To_RowInfo(My_Image)
    # X_Coords, Y_Coords = sound_and_sine.RowInfo_To_Waves(My_Image, Mean_GreyScale, Phase_Advance)
    # plt.imshow(Blank)
    # sound_and_sine.Plot_Waves(X_Coords, Y_Coords, Mean_Color, Mean_GreyScale, Phase_Advance)
    # plt.show(block=True)
    #
    # Stream, Sound_Start_Index, Sound_Sample_Rate, Phase_Adjust, EndPhase = sound_and_sine.Open_Stream()
    # PauseTime = 0.15
    #
    # Notes, Timing = image_manip.Notes_Timing_from_Image(My_Image, 128 * 4)

    # n = 0
    # while n < len(Notes):
    #     Picture_Freq = Notes[n]
    #     time.sleep(Timing[n])
    #     n+=1
    #
    # plt.pause(PauseTime * 2)
    # Stream.stop()

    ## SAVE FILE
    # wavio.write("houses.wav", np.array(Sound_Save), Sound_Sample_Rate, sampwidth=2)
    gray,rgb = image_manip.Compress_Image(My_Image,128)
    plt.imshow(PIL.Image.fromarray(gray))
    plt.waitforbuttonpress()
    plt.imshow(PIL.Image.fromarray(rgb))
    plt.waitforbuttonpress()