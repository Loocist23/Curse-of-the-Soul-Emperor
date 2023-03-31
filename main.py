#a simple text based game
#with rpg elements
#and a story that is going to be the story of my next game
#but this time it is going to be a text based game
#made by @Loocist23 on github

########################################################################################################################################################

#Imports
import random #for random numbers
import string #for string

########################################################################################################################################################

#player class
class player:
    #player variables
    name = ""
    health = 100
    attack = 10
    defense = 10
    speed = 10
    level = 1
    xp = 0
    xp_to_next_level = 100
    inventory = []

    #player functions
    def __init__(self, name):
        self.name = name

    def attack(self, enemy):
        enemy.health -= self.attack

    def defend(self, enemy):
        self.defense -= enemy.attack
    
    def level_up(self):
        self.level += 1
        self.health += 10
        self.attack += 10
        self.defense += 10
        self.speed += 10
        self.xp_to_next_level += 100