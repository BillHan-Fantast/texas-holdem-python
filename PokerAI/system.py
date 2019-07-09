###########################################################
# system.card - This file contains the System class. This class
#             controls setting up poker games and player 
#             objects. (The main class controlling the execution
#             of poker games).
# 
# author: Connor Brewton    cnb0013@auburn.edu
# created:       2/12/19
# last modified: 2/12/19
###########################################################
from pokerGame import PokerGame
from players import Player
import sys

class System:
    
    def __init__(self,players=None,buyIn=10000):
        self.game = PokerGame()
        if players==None:
            self.players = [Player("Nova",0),Player("CPU",1)]
        elif len(players) != 2:
            print("ERROR")
            sys.exit(1)
        else:
            self.players = players
        for p in self.players:
            p.chips = buyIn
    
    # return true if both players have > 0 chips
    def noPlayerIsOut(self):
        if self.players[0].chips > 0 and self.players[1].chips > 0:
            return True
        else:
            return False
    
    # reset game and players for new game
    def reset(self):
        self.game.reset()
        print(self.statusMsg())
        
    # return string representing the current state of the system
    def statusMsg(self):
        text = "=== Table Status ===\n"
        text += self.game.getStateStr() + "\n"
        for p in self.players:
            text += str(p) + "\n"
        return text
    
    # Play a hand using self.game and self.players.getAction()
    # -setup game for new hand
    # -setup players for new hand
    # -dealIn, actionPhase()
    # -flop, actionPhase()
    def playHand(self):
        print("New Hand!")
        self.reset()
        self.game.dealIn()
        self.ante()
        self.actionPhase()
        self.game.flop()
        self.actionPhase()
        self.game.turn()
        self.actionPhase()
        self.game.river()
        self.actionPhase()
        
        results = self.game.scoreHand(self.game.community_cards, self.game.hands)
        winner = self.game.findWinner(results)
        self.players[winner].chips += self.game.pot
        print("Winner is: " + str(winner) + "\n")
        
    # ante()
    def ante(self):
        self.game.pot += (50*len(self.players))
        for p in self.players:
            p.chips -= 50
        
    # actionPhase()
    # starts and controls the action phase
    def actionPhase(self):
        # player 0 turn--------------------------
        action = self.players[0].getAction(self.game)
        if action == 0:
            # player 1 wins, reset
            print("Player 0 Fold\n")
            self.players[1].chips += self.game.pot
            return 1
        elif action == 1:
            # check, continue
            print("Player 0 Check\n")
        elif action < 0:
            # error invalid action
            return 0
        elif action > self.players[0].chips:
            # error, can't bet more than you have
            return 0
        elif(not(isinstance(action,int))):
            # error, input not an integer
            return 0
        else:
            # raise amount = action, go to other player
            print("Player 0 Raise\n")
            self.players[0].chips -= action
            self.game.pot += action
            self.game.bet_amt = action
        
        # Player 1 turn------------------
        #     if bet_amt != 0, 1 is call not check
        action2 = self.players[1].getAction(self.game)
        if action2 == 0:
            # player 0 wins, reset
            print("Player 1 Fold\n")
            self.players[0].chips += self.game.pot
            return 1
        elif action2 == 1:
            # check, continue
            if self.game.bet_amt != 0:
                self.players[1].chips -= self.game.bet_amt
                self.game.pot += self.game.bet_amt
                self.game.bet_amt = 0
                print("Player 1 Call\n")
            else:
                print("Player 1 Check\n")
        elif action2 < 0:
            # error invalid action
            return 0
        elif action2 > self.players[1].chips:
            # error, can't bet more than you have
            return 0
        elif(not(isinstance(action,int))):
            # error, input not an integer
            return 0
        else:
            # raise amount = action, go to other player
            print("Player 1 Raise\n")
            self.players[1].chips -= action2
            self.game.pot += action2
        
def main():
    p1 = Player("Connor",0)
    p2 = Player("CPU",1)
    system = System([p1,p2])
    while system.noPlayerIsOut():
        print(system.statusMsg())
        system.playHand()
        print(system.statusMsg())
    
    
if __name__ == '__main__':
    main()