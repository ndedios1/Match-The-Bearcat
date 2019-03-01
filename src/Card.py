import sys
import pygame
import random

class Card:
    """
        Intializes the card class
        args: self
        return: None
    """
    def __init__(self, name):
        self.name = name + str(id(self))
        
    """
        Places rectangles (representing the cards on the game screen)
        args: self
        return: None
    """
    def placeCards(self):
        self.CARD_LEN = 100
        self.CARD_MARGIN = 10
        self.CARD_HOR_PAD = 37
        self.CARD_VER_PAD = 22
        self.ROWS = 4
        self.COLS = 5
        self.cards = [i for i in range(10) for j in range(2)]
        random.shuffle(self.cards)
        self.CARD_VAL_GRID = [self.cards[i*len(self.cards) // self.ROWS:(i+1)*len(self.cards) // self.ROWS] for i in range(self.ROWS)]
        self.CARD_GRID = [[] for i in range(self.ROWS)]
        for i in range(self.ROWS):
            if i == 0:
                for j in range(self.COLS):
                    if j == 0:
                        self.CARD_GRID[i].append(pygame.Rect(self.CARD_MARGIN, self.CARD_MARGIN, self.CARD_LEN, self.CARD_LEN))
                    else:
                        self.CARD_GRID[i].append(pygame.Rect(self.CARD_GRID[i][j-1].x + self.CARD_LEN + self.CARD_MARGIN, self.CARD_MARGIN, self.CARD_LEN, self.CARD_LEN))
            else:
                for j in range(self.COLS):
                    if j == 0:
                        self.CARD_GRID[i].append(pygame.Rect(self.CARD_MARGIN, self.CARD_GRID[i-1][0].y + self.CARD_LEN + self.CARD_MARGIN, self.CARD_LEN, self.CARD_LEN))
                    else:
                        self.CARD_GRID[i].append(pygame.Rect(self.CARD_GRID[i][j-1].x + self.CARD_LEN + self.CARD_MARGIN, self.CARD_GRID[i-1][0].y + self.CARD_LEN + self.CARD_MARGIN, self.CARD_LEN, self.CARD_LEN))
