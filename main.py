#-*- coding: utf-8 -*-
#a simple text based game
#with rpg elements
#and a story that is going to be the story of my next game
#but this time it is going to be a text based game

#made by @Loocist23 on github
########################################################################################################################################################

#Imports
import random #for random numbers
import string #for string


#made by @Loocist23 on github
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
    speciality = ""
    competence_points = 0

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
        self.competence_points += 1
        print("You leveled up!")

    
    def add_xp(self, xp):
        self.xp += xp
        if self.xp >= self.xp_to_next_level:
            self.level_up()
    
    def add_item(self, item):
        self.inventory.append(item)
    
    def remove_item(self, item):
        self.inventory.remove(item)
    
    def show_inventory(self):
        print("Your inventory:")
        for i in self.inventory:
            print(i)
    
    def show_stats(self):
        print("Your stats:")
        print("Health: " + str(self.health))
        print("Attack: " + str(self.attack))
        print("Defense: " + str(self.defense))
        print("Speed: " + str(self.speed))
        print("Level: " + str(self.level))
        print("XP: " + str(self.xp) + "/" + str(self.xp_to_next_level))
        print("Speciality: " + self.speciality)
        print("Competence points: " + str(self.competence_points))
    
    def show_all(self):
        print("Your name is " + self.name)
        self.show_stats()
        self.show_inventory()
    
#made by @Loocist23 on github
########################################################################################################################################################

#enemy class
class enemy:
    #enemy variables
    name = "" #name of the enemy
    health = 100 #health of the enemy
    attack = 10 #attack of the enemy
    defense = 10 #defense of the enemy
    speed = 10 #speed of the enemy
    level = 1 #level of the enemy
    drop = [] #drop of the enemy

    #enemy functions
    def __init__(self, name, health, attack, defense, speed, level, drop):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.level = level
        self.drop = drop
    
    def attack(self, player):
        player.health -= self.attack
    
    def defend(self, player):
        self.defense -= player.attack
    
    def level_up(self):
        self.level += 1
        self.health += 10
        self.attack += 10
        self.defense += 10
        self.speed += 10
    
    def drop_item(self):
        return self.drop[random.randint(0, len(self.drop) - 1)]
    
    def show_stats(self):
        print("Stats:")
        print("Health: " + str(self.health))
        print("Attack: " + str(self.attack))
        print("Defense: " + str(self.defense))
        print("Speed: " + str(self.speed))
        print("Level: " + str(self.level))
    
    def show_all(self):
        print("Name: " + self.name)
        self.show_stats()
        print("Drop: " + self.drop_item())
    
#made by @Loocist23 on github
########################################################################################################################################################

#item class
class item:
    #item variables
    name = "" #name of the item
    description = "" #description of the item
    type = "" #type of the item
    effect = "" #effect of the item
    value = 0 #value of the item

    #item functions
    def __init__(self, name, description, type, effect, value):
        self.name = name
        self.description = description
        self.type = type
        self.effect = effect
        self.value = value
    
    def show_all(self):
        print("Name: " + self.name)
        print("Description: " + self.description)
        print("Type: " + self.type)
        print("Effect: " + self.effect)
        print("Value: " + str(self.value))

#made by @Loocist23 on github
########################################################################################################################################################
