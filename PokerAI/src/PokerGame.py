###########################################################
# pokerGame.card - This file contains the PokerGame class.
#                A PokerGame object is created to simulate
#                a game of poker. This class handles all 
#                dealing, the deck, the hands of the players,
#                and determining the winner. 
#                Note: This class must
#                ask players for actions somehow. Create an
#                instance of PokerGame along with instances
#                of Player and call player.getAction() with
#                params from the PokerGame object
# 
# author: Connor Brewton    cnb0013@auburn.edu
# created:       2/12/19
# last modified: 2/12/19
###########################################################
from src.card import Deck
from src.players import Player
from itertools import compress, cycle

class PokerGame:
    
    # Constructor
    # create instance of a poker game.
    # 2 Players, one human, one AI, 5000 chips each
    def __init__(self,players):
        self.deck = Deck()
        self.deck.shuffle()
        self.players = players
        self.pot = 0
        self.cc = []
        self.bet_to_match = 0
        
        # init players hands and chips
        for p in self.players:
            p.chips = 5000
            p.hand = []
            
        self.still_playing = [1] * len(self.players)
        
    def playHand(self):
        self.getAntes()
        self.dealIn()
        num_alive = self.actionPhase()
        if num_alive <= 1:
            winner = self.getWinner(self.players)
            print(winner.name + " is the winner!")
            return winner
        self.flop()
        num_alive = self.actionPhase()
        if num_alive <= 1:
            winner = self.getWinner(self.players)
            print(winner.name + " is the winner!")
            return winner
        self.turn()
        num_alive = self.actionPhase()
        if num_alive <= 1:
            winner = self.getWinner(self.players)
            print(winner.name + " is the winner!")
            return winner
        self.river()
        num_alive = self.actionPhase()
        if num_alive <= 1:
            winner = self.getWinner(self.players)
            print(winner.name + " is the winner!")
            return winner
        else:
            print("Calculating winner...")
            return 0
        
    def getAntes(self):
        for p in self.players:
            if p.chips >= 50:
                p.alive = True
                p.acted = False
                p.chips -= 50
                p.bet = 50
                self.pot += 50
            else:
                p.alive = False
                p.acted = False
        self.bet_to_match = 50
    
    def dealIn(self):
        for p in self.players:
            p.hand = []
            if p.alive == True:
                p.hand.extend(self.deck.deal(2))
                
    def flop(self):
        print("Flop!")
        self.cc.extend(self.deck.deal(3))
        
    def turn(self):
        print("Turn!")
        self.cc.extend(self.deck.deal(1))
        
    def river(self):
        print("River!")
        self.cc.extend(self.deck.deal(1))
                
    def actionPhase(self):
        actionPhaseOver = False
        playerIndexList = []
        num_alive = 0
        for i in range(len(self.players)):
            playerIndexList.append(i)
            if self.players[i].alive == True:
                self.players[i].acted = False
                num_alive += 1
        pool = cycle(playerIndexList)
        
        while not actionPhaseOver and num_alive > 1:
            actingPlayerId = next(pool)
            if self.players[actingPlayerId].alive == False:
                continue
            print(self.players[actingPlayerId])
            self.printGameState()
            action = self.players[actingPlayerId].getAction()
            if action == 0:
                #Fold
                self.players[actingPlayerId].alive = False
                self.players[actingPlayerId].acted = False
                num_alive -= 1
            elif action == 1:
                # Check/Call
                self.players[actingPlayerId].alive = True
                self.players[actingPlayerId].acted = True
                if self.players[actingPlayerId].bet != self.bet_to_match:
                    diff = self.bet_to_match - self.players[actingPlayerId].bet
                    self.players[actingPlayerId].chips -= diff
                    self.pot += diff
                    self.players[actingPlayerId].bet = self.bet_to_match
            else:
                # Raise
                self.players[actingPlayerId].alive = True
                for p in self.players:
                    p.acted = False
                self.players[actingPlayerId].acted = True
                self.bet_to_match += action
                self.players[actingPlayerId].chips -= self.bet_to_match - self.players[actingPlayerId].bet
                self.players[actingPlayerId].bet = self.bet_to_match
                
            actionPhaseOver = self.checkIfActionPhaseDone(self.players)
        print(num_alive)
        
        return num_alive
        if num_alive == 1:
            winner = self.getWinner(self.players)
            print(winner.name + " is the winner!")
        else:
            print("next phase")
                
    def printPlayers(self):
        for p in self.players:
            print(p)
            
    def printPlayerHands(self):
        print("------- Player Hands -------")
        for p in self.players:
            print(p.getName() + ":\t",end=" ")
            for c in p.hand:
                print(str(c),end=" ")
            print()
            
    def printPlayerChips(self):
        print("------- Player Chip Counts -------")
        for p in self.players:
            print(p.getName() + ":\t",end=" ")
            print(p.chips)
            
    def printGameState(self):
        print("------- Game State -------")
        print("Pot: " + str(self.pot))
        print("CC: ",end=" ")
        for c in self.cc:
            print(str(c),end=" ")
        print("--------------------------")
            
    # return true if all players are alive and acted, or not alive
    def checkIfActionPhaseDone(self,players):
        result = True
        for p in players:
            if p.alive == True and p.acted == False:
                result = False
                
        return result
    
    # return the player who is alive
    def getWinner(self,players):
        for p in players:
            if p.alive == True:
                return p
    
def main():
    
    p1 = Player("Connor",0)
    p2 = Player("p2",0)
    p3 = Player("p3",0)
    p4 = Player("p4",0)
    p5 = Player("p5",0)
    players = []
    players.append(p1)
    players.append(p2)
    players.append(p3)
    players.append(p4)
    players.append(p5)
    game = PokerGame(players)
    
    game.players[2].chips = 0
    game.printPlayerHands()
    game.printPlayerChips()
    
    game.playHand()
    game.printPlayers()
    
    
    return 0

if __name__ == '__main__':
    main()
        
        
        
        