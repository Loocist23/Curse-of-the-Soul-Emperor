import random
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
