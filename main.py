"""
-*- coding: utf-8 -*-
presentation of the game
a simple text based game
with rpg elements
and a story that is going to be the story of my next game
but this time it is going to be a text based game



a litle bit of story:
so one day you woke up and you were in a house that you didn't know
first you thought that you were dreaming but then you realized that you were not
you went outside and you saw a lot of monsters
so you reentered the house and you saw a sword on the table
you took it and you started to search for equipment
you found a broken shield and a rusty helmet
you took them and you went outside again
at first the light was blinding but then you got used to it
you saw a litle girl and you asked her what happened and where you are
she told you 'What happened? You are blind ? or you are deaf ? or you are dumb ?'
you asked her again and she told you that you were in a dungeon
you asked her how you can get out and she told you that you have to kill the boss
you asked her if there is other people in the dungeon and she told you that there is
you asked her where they are and she told you that they are in the middle of the dungeon
thats when you realized that you are in a game
you asked her if she is a NPC and she told you the exact same thing
so you imediately started to search for the other people

that's all for now
i will add more story later

type of enemies:
- goblin
- skeleton
- zombie
- spider
- wolf
- bear
- baby dragon
- dragon
- demon
- angel

type of items:
- weapon
- armor
- potion
- key
- quest item

type of bosses:
- goblin king
- skeleton king
- zombie king
- spider queen
- wolf king
- bear king
- dragon king
- demon king
- god king

special enemies(ultra rare):
- Azazel
- Lucifer
- Jesus
- Mary
- Adam
- Eve
- Noah
- Abraham
- Moses
- David
- Solomon
- Elijah
- Elisha
- Isaiah
- Jeremiah
- Ezekiel

and more

special bosses(ultra ultra rare):
- God
- Devil

and more

"""

#made by @Loocist23 on github
########################################################################################################################################################


#Imports
import random #for random numbers
import string #for string
import pickle
import csv


#Importing files
from classes.player import player
from classes.enemy import enemy
from classes.item import item


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
        print("3. Heal")
        print("4. Run")
        choice = input("Your choice: ")
        if choice == "1":
            # Calculate chance of enemy evading the attack
            level_diff = enemy.level - player.level
            evasion_chance = max(0, min(50, level_diff * 5 + enemy.speed - player.speed))
            if random.randint(1, 100) <= evasion_chance:
                print(enemy.name + " evaded your attack!")
            else:
                player.attack(enemy)
                enemy.attack(player)
        elif choice == "2":
            player.defend(enemy)
            enemy.attack(player)
        elif choice == "3":
            player.heal()
        elif choice == "4":
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

#save player data
def save_player_data(player, filename):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(player.__dict__.keys())
        writer.writerow(player.__dict__.values())


#load player data
def load_player_data(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        player_data = next(reader)
        player_obj = player(**player_data) # renommer la variable pour éviter la confusion
        return player_obj




#new game function
def new_game():
    print("What is your name?")
    name = input("Your name: ")
    player1 = player(name, 100, 10, 10, 10, 1, 0, 100, [], "none", 0)
    save_player_data(player1, 'player_data.csv')
    print("Hello " + player1.name)
    return player1


#credits function
def credits():
    print("Made by @Loocist23 on github")


#game function
def game(player1):
    print("Hello " + player1.name)
    print("What do you want to do?")
    print("1. Fight")
    print("2. Inventory")
    print("3. Stats")
    print("4. Save")
    print("5. Exit")
    choice = input("Your choice: ")
    if choice == "1":
        #we will create an enemy choosen from a dict in the anemy class
        enemy1 = enemy(random.choice(list(enemy.enemies.keys())))
        fight(player1, enemy1)
    elif choice == "2":
        player1.show_inventory()
    elif choice == "3":
        player1.show_stats()
    elif choice == "4":
        save_player_data(player1, 'player_data.csv')
    elif choice == "5":
        print("Bye!")
        exit()
    else:
        print("Invalid input!")




#made by @Loocist23 on github
########################################################################################################################################################

#main
print("Welcome to the game!")
print("What do you want to do?")
print("1. New game")
print("2. Credits")
print("3. Exit")
choice = input("Your choice: ")
if choice == "1":
    player1 = new_game()
elif choice == "2":
    credits()
elif choice == "3":
    exit()
else:
    print("Invalid input!")

while True:
    game(player1)


