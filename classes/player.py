
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
    def __init__(self, name, health, attack, defense, speed, level, xp, xp_to_next_level, inventory, speciality, competence_points):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.level = level
        self.xp = xp
        self.xp_to_next_level = xp_to_next_level
        self.inventory = inventory
        self.speciality = speciality
        self.competence_points = competence_points

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
