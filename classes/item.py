
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
