#python supports classes which is a custom object
#clases can make working with specific things much easier but its rarely needed

#for instance, say we are making a game and want to make a object for the player
#in this class we will store variables such as the players cordnates and etc

class player:  #the keyword class lets python know we are trying to make a class

    #variables defined up here are private and cant be use in public scope 
    #unless there is a method that modifies it
    user_id = 1010

    #__init__ just lets python know this is the class
    # initializing function, ill explain it

    def __init__(self, username, x_cord, y_cord):

        #this is how the indivdual values are made
        self.username = username 
        self.x_cord = x_cord
        self.y_cord = y_cord 

    #these are class methods, basically functions to interact
    #with the object
    def teleport(self, new_x, new_y):
        self.x_cord = new_x
        self.y_cord = new_y

    def mod_id(self, new_id):
        print(f"users old id was {self.user_id}, the new id is {new_id}")
        self.user_id = new_id

new_player = player(username="hyka", x_cord=10, y_cord=10)
new_player.mod_id(420)
new_player.teleport(100,100)

print(f"{new_player.username}'s cords: {new_player.x_cord}, {new_player.y_cord}")

