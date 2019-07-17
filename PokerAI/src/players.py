###########################################################
# players.card - This file contains the Player class. A Player
#            object is created by pokerGame objects so that
#            there is one instance of Player for each player.
#            The Player class contains members and functions
#            that allow a player to give actions to the 
#            pokerGame object.
# 
# author: Connor Brewton    cnb0013@auburn.edu
# created:       2/12/19
# last modified: 2/12/19
###########################################################
from random import randint
# from src.card import Card
class Player:
    
    # Constructor - sets the mode and starting chips
    # for this player.
    # param: name = None, must be a string, else will use random name
    #        mode = 0 for random actions
    #               1 for human input
    #               2 for cpu simple bot
    #               3 for cpu AI bot
    #        chips = 1000, num for starting chip count, default is 1000
    def __init__(self,name=None,mode=0):
        if name == None:
            print("\nERROR: no name given!\nUsing random name...")
            self.name = "Player" + str(randint(0,9))
        elif not(isinstance(name,str)):
            print("\nERROR: name given is not a string!\nUsing random name...")
            self.name = "Player" + str(randint(0,9))
        else:
            self.name = name
        self.mode = mode
        self.chips = 0
        self.bet = 0
        self.hand = []
        self.alive = False
        self.acted = False
        
    def getName(self):
        return self.name
    
    def setName(self,nameIn):
        self.name = nameIn
        
    def getMode(self):
        return self.mode
    
    def setMode(self,modeIn):
        self.mode = modeIn
        
    def getChips(self):
        return self.chips
    
    def setChips(self,chipsIn):
        self.chips = chipsIn
        
    # Function to get actions for player. This function
    # determines what action a player will take on their turn
    # based on the player's mode and current state of the table.
    # return value: 0 for fold
    #               1 for check
    #               other int for bet amount
    def getAction(self):
        if self.mode == 0:
            # human
            action = -1
            while (action < 0 or action > self.chips):
                action = int(input("User Action: Fold(0), Call(1), Raise(type raise amount)"))
            return action
        elif self.mode == 1:
            # simple bot
            return 1
        elif self.mode == 2:
            # simple bot actions
            return 0
        elif self.mode == 3:
            # AI bot actions
            return 0
        
    # Function to print player status
    def __str__(self):
        text = "\n=== Player " + self.name + " ===\n"
        text += "Mode: " + str(self.mode) + "\n"
        text += "Chips: " + str(self.chips) + "\n"
        text += "Alive: " + str(self.alive) + "\n"
        text += "Hand: "
        for c in self.hand:
            text += str(c) + " "
        text += "\n"
        text += "==================="
        return text
        
        
def main():
    p1 = Player()
    p2 = Player("Connor",1)
    p3 = Player("Mike",0)
    p4 = Player(8,2)
    p5 = Player("Kevin",3)
    
    print(str(p1))
    print(str(p2))
    print(str(p3))
    print(str(p4))
    print(str(p5))
    
if __name__ == '__main__':
    main()