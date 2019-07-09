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
        self.big_blind_id = 0
        self.small_blind_id = 1
        self.bet_to_match = 0
        
        for p in self.players:
            p.chips = 5000
            p.hand = []
        
    def dealIn(self):
        for p in self.players:
            p.hand = []
            p.hand.extend(self.deck.deal(2))
            
    def getBlinds(self):
        self.players[self.big_blind_id].chips -= 100
        self.bet_to_match = 100
        self.players[self.small_blind_id].chips -= 50
        self.pot += 150
            
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
    
    game.dealIn()
    game.printPlayerHands()
    game.printPlayerChips()
    
    # get blinds
    game.getBlinds()
    game.printPlayerChips()
    
    # get initial actions
    
    
    return 0

if __name__ == '__main__':
    main()
        
        
        
        