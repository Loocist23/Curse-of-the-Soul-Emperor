import random
#enemy class
class enemy:
    #enemy variables
    name = "" #name of the enemy
    health = 100 #health of the enemy
    damage = 10 #damage of the enemy
    defense = 10 #defense of the enemy
    speed = 10 #speed of the enemy
    level = 1 #level of the enemy
    drop = [] #drop of the enemy

    #a dictionary of all the enemies
    enemies = {
        "goblin": {
            "name": "Goblin",
            "health": 100,
            "damage": 10,
            "defense": 10,
            "speed": 10,
            "level": 1,
            "drop": ["sword", "shield", "potion"]
        },
        "orc": {
            "name": "Orc",
            "health": 200,
            "damage": 20,
            "defense": 20,
            "speed": 20,
            "level": 2,
            "drop": ["sword", "shield", "potion"]
        },


    }


    #enemy functions 
    #init function that choose the type of enemy and sets the variables
    def __init__(self, type):
        self.name = self.enemies[type]["name"]
        self.health = self.enemies[type]["health"]
        self.damage = self.enemies[type]["damage"]
        self.defense = self.enemies[type]["defense"]
        self.speed = self.enemies[type]["speed"]
        self.level = self.enemies[type]["level"]
        self.drop = self.enemies[type]["drop"]
    
    def attack(self, other):
        other.health -= self.damage

    def defend(self, other):
        self.defense -= other.damage
    
    def level_up(self):
        self.level += 1
        self.health += 10
        self.damage += 10
        self.defense += 10
        self.speed += 10
    
    def drop_item(self):
        return self.drop[random.randint(0, len(self.drop) - 1)]
    
    def show_stats(self):
        print("Stats:")
        print("Health: " + str(self.health))
        print("Attack: " + str(self.damage))
        print("Defense: " + str(self.defense))
        print("Speed: " + str(self.speed))
        print("Level: " + str(self.level))
    
    def show_all(self):
        print("Name: " + self.name)
        self.show_stats()
        print("Drop: " + self.drop_item())
    
#made by @Loocist23 on github
########################################################################################################################################################
