#imports
from sys import exit
from random import randint
from ex45maps import *

# Engine of the game
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print "\n--------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            
            
# Death Scene            
class Death(Scene):
# One of these sentences are displayed when you die
    quips = [
        "You suck.",
         "Proud of you. not.",
         "Horrible.",
         "A goldfish is smarter."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)
        
class Win(Scene):
# One of these sentences are displayed when you win
    quips = [
        "YOU ARE THE BEST YOU WON.",
         "GREAT WORK. YOU JUST WON THE GAME",
         "ACED IT",
         "YOU WON."
    ]

    def enter(self):
        print Win.quips[randint(0, len(self.quips)-1)]
        exit(1)   
   # Map over the scenes          
class Map(object):

    scenes = {
        'death': Death(),
        'win': Win(),
        'start': Start(),
        'river': River(),
        'cross': Cross(),
        'castle': Castle()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)
        
a_map = Map('start')
a_game = Engine(a_map)
a_game.play()