import numpy as np
from matplotlib import pyplot as plt

class Helpers:
	def __init__(self):
		self.Establish_Plot()
	def Establish_Plot(self):
		Figure, Axes = plt.subplots()
		Axes.set_facecolor([0,0,0])
		Axes.set_aspect('equal')
		plt.show(block=False)
	def Example(self):
		My_Tree = Tree()
		My_Trunk = Tree_Branch(BaseNode = Node(0,0), Length = 3, Heading=np.pi/2)
		Branches = [My_Trunk]
		for n in range(5):
			Branches = My_Tree.Split_Group(Branches)
			
		Other_Trunk = Tree_Branch(BaseNode = Node(0,0), Length = 3, Heading=-np.pi/2)
		Branches = [Other_Trunk]
		for n in range(5):
			Branches = My_Tree.Split_Group(Branches)
				
class Node:
	def __init__(self, X=0, Y=0):
		#DESCRIPTION: This function is called every time a node is instantiated. 
		# A node just has an X and Y coordinate -- this is a simple class
		self.X = X
		self.Y = Y

class Tree_Branch:		
	def __init__(self, Base_Input, Length_Input, Heading_Input):
		## DESCRIPTION:
		## This function runs every time a new Tree_Branch is instantiated.
		## It assigns the properties Base, Length, and Heading. 
		## It should also call functions Grow_Tip_From_Base() and Draw()
		
		## INSTRUCTIONS:
		# First.
			# Change the function definition line to accept inputs of:
			# Base_Input, Length_Input, and Heading_Input 
			# The function definition line should then read:
			# def __init__(self, Base_Input, Length_Input, Heading_Input):
		# Second.
			# Uncomment the lines below to assign the function's inputs 
			# to this Tree_Branch instance ( and call Grow_Tip_From_Base() and Draw() ).
		
		# ~~~~~ PART 1  ~~~~~~
		## EDIT HERE ##
		## UNCOMMENT THESE 5 LINES AFTER EDITING THE FUNCTION DEFINITION LINE
		self.Base    = Base_Input
		self.Length  = Length_Input
		self.Heading = Heading_Input
		self.Tip 	  = self.Grow_Tip_From_Base()
		self.Draw()
		
		## FINISH EDITING ##
		
		return
	def Grow_Tip_From_Base(self):
		## DESCRIPTION: Find/Return tip of branch, given its base, length, and heading.
		## INSTRUCTIONS:(No action required)
		Tip = Node()
		Tip.X = self.Base.X + self.Length *np.cos(self.Heading)
		Tip.Y = self.Base.Y + self.Length *np.sin(self.Heading)
		return Tip
	def Draw(self):
		#DESCRIPTION: Draws branch onto existing plot
		#INSTRUCTIONS: (No action required)
		plt.plot([self.Base.X, self.Tip.X], [self.Base.Y, self.Tip.Y], color=[0.4,1,0.4])
		plt.draw()

class Tree:
	def __init__(self):
		#DESCRIPTION: 
		# This function is called when a Tree is instantiated. 
		# It establishes some settings, but they can always be changed later.
		
		#INSTRUCTIONS: (No action required)
		
		self.Branch_Angle = 60 *np.pi/180
		self.Branches_Per_Split = 2
		self.Branch_Length = 1
	def Split_Branch(self, Parent_Branch):
		# DESCRIPTION: 
		# Takes input of a Parent_Branch, and splits it into newly created Child Branches.
		# The base of each Child is marked as the tip of the Parent; 
		# Each child's heading is calculated
		# And a new branch is created with the given Base, Length, Heading.
		
		# INSTRUCTIONS: 
		# First.
			# Change the function definition line to accept an input of Parent_Branch
			# The definition line should read: 
			# def Split_Branch(self, Parent_Branch):
		# Second.
			# Uncomment the lines below 
			# Delete the last "return" so that this function only has one return statement.
		
		# ~~~~~ PART 3  ~~~~~~
		## EDIT HERE ##
		## UNCOMMENT THE LINES BELOW AFTER EDITING THE FUNCTION DEFINITION LINE
		
		Children      = []
		for Branch_Counter in range(My_Tree.Branches_Per_Split):
			New_Heading 	  = Parent_Branch.Heading + self.Branch_Angle*(Branch_Counter-(self.Branches_Per_Split-1)/2)  
			New_Branch        = Tree_Branch(Base_Input = Parent_Branch.Tip, Length_Input = self.Branch_Length, Heading_Input = New_Heading)
			Children.append(New_Branch)
		return Children

	def Split_Group(self, Parents):
		# DESCRIPTION: 
		# Takes input of a list of Parents, and splits each into newly created Child Branches.
		
		# INSTRUCTIONS: 
		# First.
			# Change the function definition line to accept an input of Parents
			# The definition line should read: 
			# def Split_Branch(self, Parents):
		# Second.
			# Uncomment the lines below 
			# Delete the last "return" so that this function only has one return statement.
		
		# ~~~~~ PART 4  ~~~~~~
		## EDIT HERE ##
		## UNCOMMENT THE LINES BELOW AFTER EDITING THE FUNCTION DEFINITION LINE
		Group_Children = []
		for Parent_Branch in Parents:
			Children = self.Split_Branch(Parent_Branch)
			Group_Children.extend(Children)
		return Group_Children

		
if __name__ == '__main__':


	#------------------------------------------------------------------------------------
	## ESTABLISH TREE, SETTINGS
	## (No Action Required here)
	Help = Helpers()
	My_Tree = Tree()
	My_Tree.Branch_Angle       = 60 * np.pi/180
	My_Tree.Branches_Per_Split = 2
	My_Tree.Branch_Length      = 1
	#------------------------------------------------------------------------------------
	#####################################################################################



	# ~~~~~ SECTION 4 ~~~~~~
	#____________________________________________________________________________________		
	## GROW THE TREE USING FUNCTIONS
	My_Trunk = Tree_Branch(Base_Input = Node(0,0), Length_Input = 2, Heading_Input = np.pi/2)
	Branches = [My_Trunk]
	for n in range(5):
		Branches = My_Tree.Split_Group(Branches)





	plt.waitforbuttonpress()
	
	
	