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

#functions
def fight(player, enemy):
    print("You are fighting " + enemy.name)
    while player.health > 0 and enemy.health > 0:
        print("Your health: " + str(player.health))
        print(enemy.name + "'s health: " + str(enemy.health))
        print("What do you want to do?")
        print("1. Attack")
        print("2. Defend")
        print("3. Run")
        choice = input("Your choice: ")
        if choice == "1":
            player.attack(enemy)
            enemy.defend(player)
        elif choice == "2":
            player.defend(enemy)
            enemy.attack(player)
        elif choice == "3":
            #there is a small chance that you will not be able to run away
            if random.randint(0, 100) > random.randint(0, 50):
                print("You ran away!")
                break
            else:
                print("You couldn't run away!")
                enemy.attack(player)
        else:
            print("Invalid input!")
        if enemy.health <= 0:
            print("You won!")
            print("You got " + enemy.drop_item())
            player.add_item(enemy.drop_item())
            player.add_xp(10)
            break
        elif player.health <= 0:
            print("You lost!")
            break
        else:
            continue

#made by @Loocist23 on github
########################################################################################################################################################

#main
#function to create a new player
def new_player():
    name = input("Your name: ")
    player = player(name)
    return player

#function to load a player
def load_player():
    name = input("Your name: ")
    player = player(name)
    #load player stats from a file
    return player

#function to save a player
def save_player(player):
    #save player stats to a file
    return

#function to show the main menu
def main_menu():
    print("Welcome to the game!")
    print("1. New game")
    print("2. Load game")
    print("3. Exit")
    choice = input("Your choice: ")
    if choice == "1":
        player = new_player()
        return player
    elif choice == "2":
        player = load_player()
        return player
    elif choice == "3":
        return
    else:
        print("Invalid input!")
        main_menu()

#function to show the game menu
def game_menu(player):
    print("1. Show stats")
    print("2. Show inventory")
    print("3. Save game")
    print("4. Exit")
    choice = input("Your choice: ")
    if choice == "1":
        player.show_stats()
        game_menu(player)
    elif choice == "2":
        player.show_inventory()
        game_menu(player)
    elif choice == "3":
        save_player(player)
        game_menu(player)
    elif choice == "4":
        return
    else:
        print("Invalid input!")
        game_menu(player)

