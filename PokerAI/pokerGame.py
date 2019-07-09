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
from card import Deck

class PokerGame:
    
    # Constructor
    # create instance of a poker game.
    # 2 Players, one human, one AI, 5000 chips each
    def __init__(self,num_players=2):
        self.deck = Deck()
        self.hands = []
        self.community_cards = []
        self.num_players = num_players
        self.pot = 0
        self.bet_amt = 0
        
    # shuffle function, just shuffles deck
    def shuffle(self):
        self.deck.shuffle()
        
    # reset the game state for a new hand
    def reset(self):
        self.shuffle()
        self.community_cards = []
        self.hands = []
        self.pot = 0
        
    # deal in 2 card to all players
    # returns a list of hands
    def dealIn(self):
        for i in range(self.num_players):
            hand = []
            hand.extend(self.deck.deal(2))
            self.hands.append(hand)
        
        # debug, print hands
#         print(self.getStateStr())
        
    # flop
    # deals 3 card to community card
    def flop(self):
        print("Flop!")
        self.community_cards = self.deck.deal(3)
        
        # debug, print table
        print(self.getStateStr())
        
    # turn
    # deals 1 card to community card
    def turn(self):
        print("Turn!")
        self.community_cards.extend(self.deck.deal(1))
        
        # debug, print table
        print(self.getStateStr())
        
    # river
    # deals 1 card to community card
    def river(self):
        print("River!")
        self.community_cards.extend(self.deck.deal(1))
        
        # debug, print table
        print(self.getStateStr())
        
    # assign hand types a label
    def handLabel(self, hand_type):
        if hand_type == 0:
            return "High Card"
        elif hand_type == 1:
            return "Pair"
        elif hand_type == 2:
            return "Two Pair"
        elif hand_type == 3:
            return "Three of a Kind"
        elif hand_type == 4:
            return "Straight"
        elif hand_type == 5:
            return "Flush"
        elif hand_type == 6:
            return "Full House"
        elif hand_type == 7:
            return "Four of a Kind"
        elif hand_type == 8:
            return "Straight Flush"
        else:
            return "Royal Flush"
        
    # get str representation of hand
    # param: hand is a list with any number of card
    # return a str displaying each card in hand
    def cards2Str(self,hand):
        text = ""
        for c in hand:
            text += str(c) + " "
        return text
    
    # check if hand has a pair
    # return -1 if no, value of highest pair if yes
    def hasPair(self,hand):
        self.sortHand(hand)
        print(self.cards2Str(hand))
        result = -1
        for c in hand:
            for c2 in hand:
                if c.value == c2.value and c.suit != c2.suit:
                    result = c.value
        return result
    
    # check if hand has 3 of a kind
    # return -1 if no, value of 3 if yes
    def has3ofKind(self,hand):
        self.sortHand(hand)
        print(self.cards2Str(hand))
        result = -1
        for c in hand:
            num = 0
            for c2 in hand:
                if c2.value == c.value:
                    num += 1
            if num >= 3:
                result = c2.value
        return result            
    
    # sort 7 card hand by card.value
    def sortHand(self,hand):
        hand.sort(key=lambda x: x.value)
        
    # getStateStr()
    # function prints all values related to current game state
    # returns str representation of state
    def getStateStr(self):
        text = "=== Current Hand State ===\n"
        text += "Community Cards: " + self.cards2Str(self.community_cards) + "\n"
        for h in self.hands:
            text += self.cards2Str(h) + "\n"
        text += "Pot: " + str(self.pot) + "\n"
        text += "========================="
        return text
    
    # score()
    # scores the best 5 card hand given 7 card
    # param: hand to score
    # returns an int between 0 and 9 representing score
    def score(self,hand):
        score = 0
        kicker = []
        # Look for all hand types in hand
        # start with weakest and move up

        # check for pairs first
        pairs = {}
        prev = 0

        # remember how many pairs you have, which pairs
        for card in hand:
            if prev == card.value:
                key = card.value
                if key in pairs:
                    pairs[key] += 1
                else:
                    pairs[key] = 2
            prev = card.value

        # remember number of pairs.
        nop = {}
        for k, v in pairs.items():
            if v in nop:
                nop[v] += 1
            else:
                nop[v] = 1
        # find best possible combination
        if 4 in nop:
            score = 7
            kicker = list(pairs)
            kicker = [key for key in kicker if pairs[key] == 4]
            key = kicker[0]
            #Gets a list of all the card remaining once the the 4 of a kind is removed
            temp = [card.value for card in hand if card.value != key]
            #Get the final card in the list which is the highest card left, used in 
            #case of a tie
            card_value = temp.pop()
            kicker.append(card_value)

            return [score, kicker]

        elif 3 in nop:        #Has At least 3 of A Kind
            if nop[3] == 2 or 2 in nop:        #Has two 3 of a kind, or a pair and 3 of a kind (fullhouse)
                score = 6

                #gets a list of all the pairs and reverses it
                kicker = list(pairs)
                kicker.reverse()
                temp = kicker

                #ensures the first kicker is the value of the highest 3 of a king
                kicker = [key for key in kicker if pairs[key] == 3]
                if( len(kicker) > 1):   # if there are two 3 of a kinds, take the higher as the first kicker
                    kicker.pop() #removes the lower one from the kicker

                #removes the value of the kicker already in the list
                temp.remove(kicker[0])
                #Gets the highest pair or 3 of kind and adds that to the kickers list
                card_value = temp[0]
                kicker.append(card_value)

            else:            #Has Only 3 of A Kind
                score = 3

                kicker = list(pairs)        #Gets the value of the 3 of a king
                key = kicker[0]

                #Gets a list of all the card remaining once the three of a kind is removed
                temp = [card.value for card in hand if card.value != key]
                #Get the 2 last card in the list which are the 2 highest to be used in the 
                #event of a tie
                card_value = temp.pop()
                kicker.append(card_value)

                card_value = temp.pop()
                kicker.append(card_value)

        elif 2 in nop:    #Has at Least a Pair
            if nop[2] >= 2:        #Has at least 2  or 3 pairs
                score = 2

                kicker = list(pairs)    #Gets the card value of all the pairs 
                kicker.reverse()        #reverses the key so highest pairs are used

                if ( len(kicker) == 3 ):    #if the user has 3 pairs takes only the highest 2
                    kicker.pop()

                key1 = kicker[0]
                key2 = kicker[1]

                #Gets a list of all the card remaining once the the 2 pairs are removed
                temp = [card.value for card in hand if card.value != key1 and card.value != key2]
                #Gets the last card in the list which is the highest remaining card to be used in 
                #the event of a tie
                if len(temp) != 0:
                    card_value = temp.pop()
                else:
                    card_value = 0
                kicker.append(card_value)

            else:        #Has only a pair
                score = 1 

                kicker = list(pairs)   #Gets the value of the pair
                key = kicker[0] 

                #Gets a list of all the card remaining once pair are removed
                temp = [card.value for card in hand if card.value != key]
                #Gets the last 3 card in the list which are the highest remaining card
                #which will be used in the event of a tie
                card_value = temp.pop()
                kicker.append(card_value)

                card_value = temp.pop()
                kicker.append(card_value)

                card_value = temp.pop()
                kicker.append(card_value)


        # Straight???   
        #Doesn't check for the ace low straight
        counter = 0
        high = 0
        straight = False

        #Checks to see if the hand contains an ace, and if so starts checking for the straight
        #using an ace low
        if (hand[6].value == 14): 
            prev = 1
        else: 
            prev = None

            #Loops through the hand checking for the straight by comparing the current card to the
            #the previous one and tabulates the number of card found in a row
            #***It ignores pairs by skipping over card that are similar to the previous one
        for card in hand:
            if prev and card.value == (prev + 1):
                counter += 1
                if counter == 4: #A straight has been recognized
                    straight = True
                    high = card.value
            elif prev and prev == card.value: #ignores pairs when checking for the straight
                pass
            else:
                counter = 0
            prev = card.value

        #If a straight has been realized and the hand has a lower score than a straight
        if (straight or counter >= 4) and score < 4:
            straight = True  
            score = 4
            kicker = [high] #Records the highest card value in the straight in the event of a tie


        # Flush???
        flush = False
        total = {}

        #Loops through the hand calculating the number of card of each symbol.
        #The symbol value is the key and for every occurrence the counter is incremented
        for card in hand:
            key = card.suit
            if key in total:
                total[key] += 1
            else:
                total[key] = 1

        #key represents the suit of a flush if it is within the hand
        key = -1
        for k, v in total.items():
            if v >= 5:
                key = int(k)

        #If a flush has been realized and the hand has a lower score than a flush
        if key != -1 and score < 5:
            flush = True
            score = 5
            kicker = [card.value for card in hand if card.suit == key]        


        #Straight/Royal Flush???
        if flush and straight:

            #Doesn't check for the ace low straight
            counter = 0
            high = 0
            straight_flush = False

            #Checks to see if the hand contains an ace, and if so starts checking for the straight
            #using an ace low
            if (kicker[len(kicker)-1] == 14): 
                prev = 1
            else: 
                prev = None

            #Loops through the hand checking for the straight by comparing the current card to the
            #the previous one and tabulates the number of card found in a row
            #***It ignores pairs by skipping over card that are similar to the previous one
            for card in kicker:
                if prev and card == (prev + 1):
                    counter += 1
                    if counter >= 4: #A straight has been recognized
                        straight_flush = True
                        high = card
                elif prev and prev == card: #ignores pairs when checking for the straight
                    pass
                else:
                    counter = 0
                prev = card

            #If a straight has been realized and the hand has a lower score than a straight
            if straight_flush:
                if high == 14:
                    score = 9
                else:
                    score = 8
                kicker = [high]
                return [score, kicker]

        if flush:        #if there is only a flush then determines the kickers
            kicker.reverse()

            #This ensures only the top 5 kickers are selected and not more.
            length = len(kicker) - 5
            for i in range (0,length):
                kicker.pop() #Pops the last card of the list which is the lowest

        # High Card
        if score == 0:        #If the score is 0 then high card is the best possible hand

            #It will keep track of only the card's value
            kicker = [int(card.value) for card in hand]
            #Reverses the list for easy comparison in the event of a tie
            kicker.reverse()
            #Since the hand is sorted it will pop the two lowest card position 0, 1 of the list
            kicker.pop()
            kicker.pop()
            #The reason we reverse then pop is because lists are inefficient at popping from
            #the beginning of the list, but fast at popping from the end therefore we reverse 
            #the list and then pop the last two elements which will be the two lowest card
            #in the hand        

        #Return the score, and the kicker to be used in the event of a tie
        return [score, kicker]
        
        
    # getWinner()
    # this function calculates the winner of the
    # hand given the current game state.
    # returns the index of the winning player
#     def getWinner(self):

    def scoreHand(self, community_cards, hands):
        for hand in hands:
            hand.extend(community_cards)
            # sort hands
#             hand.sort(key=lambda x: x.value)
            self.sortHand(hand)
        
        results = []
        for hand in hands:
            overall = self.score(hand)
            results.append([overall[0], overall[1]])    # store results

        return results
    
    #determine winner of round
    def findWinner(self, results):
        # show hands TODO: update printing hands with best hand label
        print("Finding Winner...")
        for i in range(len(results)):
            text = ""
            text += self.cards2Str(self.hands[i]) + " " + self.handLabel(results[i][0])
            print(text)
        # highest score if found
        high = 0
        for r in results:
            if r[0] > high:
                high = r[0]

            # print(r)

        kicker = {}
        counter = 0
        # kickers only compared if hands are tied (haha, hands are tied)
        for r in results:
            if r[0] == high:
                kicker[counter] = r[1]

            counter += 1

        # if kickers of multiple players are here, there is a tie
        if(len(kicker) > 1):
            print("Tie. Kickers:")
            for k, v in kicker.items():
                print(str(k) + " : " + str(v))
            num_kickers = len(kicker[list(kicker).pop()])
            for i in range(0, num_kickers):
                high = 0
                for k, v in kicker.items():
                    if v[i] > high:
                        high = v[i]

                # only hands with highest kicker matching compared
                kicker = {k:v for k, v in kicker.items() if v[i] == high}
                print("---Round " + str(i) + " ---")
                for k in kicker:
                    print(k)

                # if only one kicker remains they win
                if (len(kicker) <= 1):
                    return list(kicker).pop()

        else:    # one winner found, no kickers needed
            return list(kicker).pop()

        # tie, return list of winners
        return list(kicker)
        
        
def main():
    # start a new game
    game = PokerGame()
    game.reset()
    game.dealIn()
    game.flop()
    game.turn()
    game.river()
    results = game.scoreHand(game.community_cards, game.hands)
    winner = game.findWinner(results)
    print("Winner is: " + str(winner))
#     hand = game.deck.deal(7)
#     print(str(game.has3ofKind(hand)))
    
    
if __name__ == '__main__':
    main()