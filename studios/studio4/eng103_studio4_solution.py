import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import animation as anim
import time as timepack
import sounddevice as sd
import wavio

sd.default.latency = ('high')


class Helpers:

	def Initialize(self):
		self.Harmonograph_Settings()
		self.Establish_Sound()
		self.Establish_Plot(Independent_Variable_Length = 3200)				
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
		Line_Length = 18 # How many cycles to draw the trace during graphing
		Disharmony = 0/32 # Introduce disharmony (mismatch between fx and fy) for more interesting results
		Phase_Common =0  # Add phase to both sinusoids
		Phase_Differential = np.pi/4 # Add phase to only one sinusoid
		fx = 1 # Frequency tied to x axis (usually lower note)
		fy = 1 # Frequency tied to y axis (usually higher note)
		Note_Titles = ['Root/Octave', 'step', '2nd', '3rd (minor)', '3rd (Major)', '4th (Perfect)', 'Tritone', '5th (Perfect)', '6th (Minor)', '6th (Major)', '7th (Minor)', '7th (Major)', 'Octave', 'Octave +']

		## SETTINGS FOR PAUSE AND HOLD WHILE PLAYING NOTE
		NoteHold_Time = 1 # How long to hold each note -- just a default, likely overwritten by 'Timing' during 'Play_Notes'
		NoteHold_Phase_Rotation = np.pi/6 # How much the differential phase moves during note (looks like rotating figure)
		NoteHold_Steps_Per_Second = 60 # How many steps to take as figure rotates (more steps looks like smoother rotation))
		Graph_Update_Interval_ms = 20 # How long the graph waits between updates, in milliseconds.
		
		## SETTINGS FOR SOUND GENERATION
		Base_Freq = 440/4 # This frequency corresponds to our "Root" note -- 440 Hz is middle A.
		Sound_Block_Size = 2000 # How many sound samples are processed at a time. there are 44100 in a second.
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
		Sound_Sample_Rate = 44100
		StrikeTime=0
		Sound_Save = []
		
		## INITIATE CONNECTION TO SPEAKER
		Stream = sd.OutputStream(samplerate = Sound_Sample_Rate, callback = self.Sound_Callback, blocksize = Sound_Block_Size) #Define connection between code and speaker (ESPECIALLY IMPORTANT callback function provided for sound generation)
		Stream.start() #Start sending data from code to speaker
		sd.wait() #Don't terminate the sound until we say so
		

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
		fx_graph=1
		fy_graph=1
		plt.ion() #Turn on interactive mode
		Figure, ax = plt.subplots() #Create figure and axes
		x = np.linspace(-1,1,Independent_Variable_Length) #Create x coordinates for line -- will be changed every time callback is called.
		y = x #Create y coordinates for line
		My_Line, = ax.plot(x, y, lw=2) ## Plot the line, with data to be updated during animation.
		plt.show() #display plot
		Animation = anim.FuncAnimation(fig=Figure, func=self.Plot_Callback, frames=None, fargs = [My_Line], interval=Graph_Update_Interval_ms) #Create animation. Specify figure, callback function, and interval. "fargs" passes inputs to callback.
		My_Line._color  =  0.9*np.array([np.cos(2*np.pi*(0/12+2/3)),np.cos(2*np.pi*(0/12 +1/3)),np.cos(2*np.pi*(0/12 +0/3))])/2+0.5 #Start line with pretty color. 
		plt.pause(0.01)
		return 
	def Sound_Callback(self, outdata, frames, time, status):
		
		## DESCRIPTION ##
		## (No need to edit this function)
		## This function generates the sound that is sent to the speakers. It is assigned to 
		## the previously created STREAM, so that any time the STREAM calls this function 
		## any time it needs more sound data generated.
		
		global Sound_Start_Index
		#Establish time sequence
		t = (Sound_Start_Index + np.arange(frames)) / Sound_Sample_Rate
		
		#Create sound sinewaves
		Note1 = np.sin(2*np.pi*t*Base_Freq*fx+ Phase_Common)
		Note2 = np.sin(2*np.pi*t*Base_Freq*fy+ Phase_Common + Phase_Differential)
		Sound = Note1/3 + Note2
		#Fade volume over time
		Sound =  np.multiply(Sound, np.exp(-((timepack.time() - StrikeTime+ t-t[0] )/NoteHold_Time)**2))

		#Write Sound to stream's "outdata"
		outdata[:] = Sound.reshape(-1,1)
		Sound_Save.extend(Sound.reshape(-1,1))
		
		#Advance starting time for next sound block
		
		Sound_Start_Index += frames			
	def Plot_Callback(self, frame, Line):
		## DESCRIPTION ##
		## (No need to edit this function)
		## This function tells the animated graph what to draw.
		## It is called every INTERVAL (usually less than a second) defined in the Establish_Plot function
		## The crucial step is in the commands Line.set_xdata and Line.set_ydata
		
		Amplitude = np.exp(-((timepack.time() - StrikeTime )/NoteHold_Time)**2)**(1/3)
		#HOUSEKEEPING -- establish time sequence and disharmony
		t = np.linspace(0,Line_Length, np.size(Line.get_xdata()))		
		Disharmony_Mult = Disharmony/Line_Length/np.max([fy_graph, 0.1])
		
		## LINEAR HARMONOGRAPH -- control x and y coordinates with sine waves of different frequencies
		X_Linear = np.sin(2*np.pi*fx_graph*t+Phase_Common) #Sinewave at frequency fx. Add common phase
		Y_Linear = np.sin(2*np.pi*fy_graph*t*(1+Disharmony_Mult) + Phase_Differential + Phase_Common) 
		
		## ROTARY HARMONOGRAPH -- control x and y coordinates with circles of different frequencies
		Circle1x = np.cos(2*np.pi*fx_graph*t*(1+Disharmony_Mult)+Phase_Common+ Phase_Differential)
		Circle1y = np.sin(2*np.pi*fx_graph*t*(1+Disharmony_Mult)+Phase_Common+ Phase_Differential)		
		Circle2x = np.cos(2*np.pi*fy_graph*t+Phase_Common)
		Circle2y = np.sin(2*np.pi*fy_graph*t+Phase_Common)		
		X_Rotary = (Circle1x-Circle2y)/2
		Y_Rotary = (Circle1y-Circle2x)/2
		
		## ASSIGN DATA TO LINE (FEEL FREE TO PICK X/Y_LINEAR OR X/Y_ROTARY)
		Line.set_xdata(  X_Linear  *Amplitude)  # update the data
		Line.set_ydata(  Y_Rotary  *Amplitude)  # update the data
		plt.draw() #Draw updated data
		
	def Play_Note(self, Note, Duration=1):
		## DESCRIPTION
		## This function controls the parameters that define the sound and graph.
		## Although there are no direct calls to graph and sound generation in here,
		## the variables that are changed do influence the graph and sound. 
		
		#Establish global parameters so the edits here make changes in graph/sound callbacks
		global fx
		global fy
		global fy_graph
		global Phase_Differential
		global Phase_Common
		global StrikeTime
		global My_Line
		
		#Update note frequency and strike time
		fy = 2**(Note/12) #Change fy
		fy_graph=fy #Update graph
		StrikeTime = timepack.time() #Record time of striking this note
		#Add title
		plt.title(Note_Titles[int(np.log2(fy/fx)*12.01)%12])
		My_Line._color  = 0.9 * np.array([np.cos(2*np.pi*(Note/12+2/3)),np.cos(2*np.pi*(Note/12 +1/3)),np.cos(2*np.pi*(Note/12 +0/3))])/2+0.5
		plt.pause(1e-6)
		# Pause on this note
		NoteHold_Steps = int(NoteHold_Steps_Per_Second*Duration)+1
		for NoteHold_Step in range(NoteHold_Steps):
			Phase_Differential += NoteHold_Phase_Rotation/NoteHold_Steps #Add to phase difference between sinusoids
			plt.pause(1e-6)
			timepack.sleep(Duration/NoteHold_Steps)
	def Transition_Between_Notes(self, Note1, Note2, Transition_Time=0.1):
		## DESCRIPTION
		## This function controls the parameters that define the sound and graph.
		## It only affects the graph, not the sound. 
		## Although there are no direct calls to graph and sound generation in here,
		## the variables that are changed do influence the graph and sound. 
		
		global Line_Length
		global My_Line
		global fy_graph
		#Initiate transition to next note
		Line_Length_Original = Line_Length
		Transition_Steps = int(Transition_Time * NoteHold_Steps_Per_Second) + 1
		Transition_Pause = Transition_Time/Transition_Steps
		for T in range(Transition_Steps):
			Quadratic_Shape_Fn = ((T - (Transition_Steps/2))/(Transition_Steps/2))**2 +0.01 #Shorten and regrow tail of figure during transition
			Note_Transition = (Note1*(1-(T+1)/Transition_Steps) + Note2*(T+1)/Transition_Steps)
			Line_Length = Line_Length_Original * Quadratic_Shape_Fn
			My_Line._linewidth = 3 * Quadratic_Shape_Fn
			My_Line._color  = Quadratic_Shape_Fn*0.9 * np.array([np.cos(2*np.pi*(Note_Transition/12+2/3)),np.cos(2*np.pi*(Note_Transition/12 +1/3)),np.cos(2*np.pi*(Note_Transition/12 +0/3))])/2+0.5
			fy_graph = 2**(Note_Transition/12)
			fy=fy_graph
			plt.pause(1e-6)
			timepack.sleep(Transition_Pause)
		Line_Length = Line_Length_Original #Set figure back to full tail length again

	def Major_Scale(self):
		Notes = [0,2,4,5,7,9,11,12,11,9,7,5,4,2,0]
		Timing = np.ones((len(Notes)))*0.5
		return Notes, Timing
	def Minor_Scale(self):
		Notes = [0,2,3,5,7,8,10,12,10,8,7,5,3,2,0]
		Timing = np.ones((len(Notes)))*0.5
		return Notes, Timing
	def Blues_Scale(self):
		Q = 0.25 - Transition_Pause
		E = Q/2
		S = Q/4
		Notes = [0,3,5,6,7,10,12,10,7,6,5,3,0]
		Timing =[Q,Q,S,S,E, Q, Q, Q,S,S,E,Q,Q]
		return Notes, Timing
	def Blues_Riff(self):
		global Transition_Steps
		global Transition_Duration
		global Transition_Pause
		Transition_Steps = 10
		Transition_Duration = 0.00625
		Transition_Pause = Transition_Duration/Transition_Steps
		Beat = 0.5
		T1 = np.max([0, Beat/1 - Transition_Duration])
		T2 = np.max([0, Beat/2 - Transition_Duration])
		T4 = np.max([0, Beat/4 - Transition_Duration])
		T8 = np.max([0, Beat/8 - Transition_Duration])
								
		Notes =  [0,   5,         3,  0,   -1000,     0, -1000, 0,   -1000,      0, -1000,  0,   -1000]
		Timing = [T4, T2+T4, (T8+T4/2), T4,     T4,    T8,     0,T4,      T4,     T8,     0, T4,      T4]
		Notes = Notes+Notes+Notes
		Timing = np.array(Timing + Timing+Timing)*2
		Timing[-1] *=10
		return Notes, Timing
	def Fur_Elise(self):
		Notes = [7,6,7,6,7,2, 5, 3, 0]
		Timing = np.ones((len(Notes)))*0.1
		Timing[-1] *=10
		return Notes, Timing
		
		
if __name__ == '__main__':
	## ESTABLISH PLOT, SOUND STREAM, HARMONOGRAPH BEHAVIOR
	Jeeves = Helpers()
	Jeeves.Initialize()



	## EXAMPLE SONG -- EDIT THIS OR START FROM SCRATCH
	##________________________________________________
	#NoteHold_Time = 1
	#Jeeves.Play_Note(Note=0, Duration = 0.3)
	#Jeeves.Transition_Between_Notes(Note1=0, Note2 = 4, Transition_Time=0.5) # This function only affects the graph
	
	#Jeeves.Play_Note(Note=4, Duration = 0.3)
	#Jeeves.Transition_Between_Notes(Note1=4, Note2 = 7, Transition_Time=0.5) # This function only affects the graph	
	
	#Jeeves.Play_Note(Note=7, Duration = 0.3)
	#Jeeves.Play_Note(Note=4, Duration = 0.3)
	#Jeeves.Play_Note(Note=0, Duration = 0.3)	
	##________________________________________________
	
	
	
	##________________________________________________
	## PART 2 ##
	# Write your own song using the function Play_Note()
	# Play several notes in a row. 
	##________________________________________________
	
	
	##________________________________________________
	## PART 3 ##
	## Write your loops here to create music. 
	##________________________________________________
	
	
	
	Beat = 0.3
	while 1:
		for i in range(3):
			NoteHold_Time = 0.1
			Jeeves.Play_Note(Note=0, Duration = Beat*2/3)
			Jeeves.Play_Note(Note=12, Duration = Beat/3)
			Jeeves.Play_Note(Note=24, Duration = Beat*2/3)
			Jeeves.Play_Note(Note=36, Duration = Beat/3)		
		
			NoteHold_Time = 0.5
			Jeeves.Play_Note(Note=0, Duration = Beat*2/3)
			Jeeves.Play_Note(Note=12, Duration = Beat/3)
			Jeeves.Play_Note(Note=24, Duration = Beat*2/3)
			Jeeves.Play_Note(Note=36, Duration = Beat/3)	
	
			NoteHold_Time = 0.1
			Jeeves.Play_Note(Note=0, Duration = Beat*2/3)
			Jeeves.Play_Note(Note=12, Duration = Beat/3)
			Jeeves.Play_Note(Note=24, Duration = Beat*2/3)
			Jeeves.Play_Note(Note=36, Duration = Beat/3)	
		
			NoteHold_Time = 0.4
			Jeeves.Play_Note(Note=0, Duration = Beat*2)
		
		NoteHold_Time = 0.3
		Jeeves.Play_Note(Note=7+12, Duration = Beat)
		Jeeves.Play_Note(Note=7+12, Duration = Beat)
		Jeeves.Play_Note(Note=5+12, Duration = Beat)
		Jeeves.Play_Note(Note=5+12, Duration = Beat)
		Jeeves.Play_Note(Note=3+12, Duration = Beat)	
		Jeeves.Play_Note(Note=3+12, Duration = Beat)
		Jeeves.Play_Note(Note=2+12, Duration = Beat)			
		Jeeves.Play_Note(Note=2+12, Duration = Beat)	

	## SAVE FILE
	wavio.write("Rivard_Carson_Part2.wav", np.array(Sound_Save), Sound_Sample_Rate, sampwidth=2)
	
	## CLOSE OUT
	Stream.stop()
	plt.waitforbuttonpress()