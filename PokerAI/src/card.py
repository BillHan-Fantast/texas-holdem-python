###########################################################
# cards.py - This file contains the Card class and Deck
#            class.
# 
# author: Connor Brewton    cnb0013@auburn.edu
# created:       2/12/19
# last modified: 2/12/19
###########################################################
# import sys
import random
# import math
# import numpy as np
# import matplotlib.pyplot as plt

class Card:

    def __init__(self,suit,value):
        self.suit = suit
        self.value = value

    # compare value of two cards
    def __cmp__(self, other):
        if self.value < other.value:
            return -1
        elif self.value == other.value:
            return 0
        return 1

    # compare suit of two cards
    #    returns 1 if suits match
    def cmpSuit(self, other):
        if self.suit == other.suit:
            return 1
        else:
            return 0

    # get a string for given card
    def __str__(self):
        text = ""
        # set value text
        if self.value == 11:
            text = "J"
        elif self.value == 12:
            text = "Q"
        elif self.value == 13:
            text = "K"
        elif self.value == 14:
            text = "A"
        else:
            text = str(self.value)

        if self.suit == 0:
            text += "H"
        elif self.suit == 1:
            text += "C"
        elif self.suit == 2:
            text += "D"
        elif self.suit == 3:
            text += "S"
        else:
            text += "?"

        return text

class Deck:

    # init the deck by adding 52 unique cards
    # self.cards = [] of 52 unique cards
    # self.drawnCards = [] cards popped by deal() stored here
    #    returned when shuffle() called
    def __init__(self):
        self.cards = []
        self.drawnCards = []
        for suit in range(0,4):
            for value in range(2,15):
                self.cards.append(Card(suit,value))
#         self.num_cards = 52

    # restore drawnCards to deck and shuffle
    def shuffle(self):
        self.cards.extend(self.drawnCards)
        self.drawnCards = []
        random.shuffle(self.cards)

    # deal num_cards
    # return [] of cards len = num_cards
    # cards drawn are popped and added to drawnCards
    def deal(self,num_cards):
        if (num_cards > len(self.cards)):
            return False
        drawnCards = []
        for i in range(0, num_cards):
            drawnCards.append(self.cards.pop(0))
        self.drawnCards.extend(drawnCards)
        return drawnCards

    # returns the number of cards left in deck
    def cardsLeft(self):
        return len(self.cards)
    
    # print the deck
    def printDeck(self):
        text = "Deck\n"
        i = 0
        for c in self.cards:
            if i == 4:
                i = 0
                text += str(c) + "\n"
            else:
                i += 1
                text += str(c) + ","
        print(text)
    
# main function only used to test card functions,
# this file should be a library file to import Card/Deck classes
def main():
    
    deck = Deck()
    deck.printDeck()
    deck.shuffle()
    deck.printDeck()
    
if __name__ == '__main__':
    main()