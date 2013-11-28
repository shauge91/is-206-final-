axe = False #global variable declared

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)
        
# First scene
class Start(Scene):

    def enter(self):
   		print "You are the Prince of Sibiria"
   		print "You are going to save a captured princess who is held hostage by the evil dragon"
		print "in his big fortress in the deep forest of Cappucia."
		print "You have a long way ahead of you, and you choose to bring your horse Golden eye."
		print "When you reach a river, to wide for Golden eye to jump across you must make a choice."
		print "Do you follow the river left or right in your search for a better place to cross? (left or right)"
		
		action = raw_input("> ")
		#if you choose to walk left, you enter the river scene
		if action == "left":
			print "you choose to walk left"
			return 'river'
		
		# If you choose to walk right you enter the cross scene
		elif action == "right":
			print "you choose to walk right"
			return 'cross'
		
		# If you don't make a valid choice, you die.
		else:
			print "You die because you didn't make up your mind You starved to death"
			return 'death'

# Class River             
class River(Scene):
	
	def enter(self):
		print "It is obvious that you need to turn around"
		print "Behind a tree you see an abondoned axe"
		print "Pick up the axe and then turn around (turn around)"
		global axe #declares a global variable
		axe = True #sets the global variable to true
		if axe == True:  #if it was set as True, it prints a text
			print "You picked up the axe" 
		action = raw_input("> ")
        
        # if you turn around you enter the scene cross
		if action == "turn around":
			print "you choose to turn around"
			return 'cross'
        
        # If you do something else, you die.
		else:
			print "You fell into the river."
			return 'death'

# Class Cross
class Cross(Scene):

    def enter(self):
		print "The river gets narrower and narrower"
		print "Make your horse jump across the river (jump)"
	
		action = raw_input("> ")
		
		# If you jump, you enter the castle scene
		if action == "jump":
			print "You jump across the river"
			return 'castle'
		
		# If you do anything else, you die.
		else:
			print "You drown because you didn't jump"
			return "death"

# Class Castle, last scene
class Castle(Scene):

    def enter(self):
		print "At last you reach the castle."
		print "When you try to enter, the evil dragon appears."
		print "What do you do? Fight or run?"
		
		action = raw_input("> ")

		# If you fight and the global variable axe is false. You die.
		if action == "fight" and axe == False:
			print "You tried to fight the dragon" 
			print "But didn't have an axe. You died."
			return 'death'
		
		# If you fight and the global variable is True. You win
		elif action == "fight" and axe == True:
			print "You fought the dragon" 
			print "You have an axe. You won"
			return 'win'
		
		# If you choose run, you die
		elif action == "run": 
			print "the dragon kills you." 
			return 'death'
		
		# If anything else is written, you die
		else:
			print "You didn't make up your mind. You die."
			return 'death'
