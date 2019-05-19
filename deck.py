from enum import Enum
from card import Card
import random

class DeckType(Enum):
    Card36 = 1,
    Card52 = 2

class Deck:
    __suits = ['♦','♥','♣','♠']
    __cardset = {'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'10': 10,'В': 11,'Д': 12,'К': 13,'Т': 14}

    def __init__(self, deckType):
        if(type(deckType) != DeckType): raise Exception('Некорректный тип колоды')
        self.__deckType = deckType

    def fillDeck(self):
        self.cards = []
        iterator = 1

        # # TODO убрать
        # self.cards.append(Card('6', '♥', 1, 1))
        # self.cards.append(Card('7', '♥', 1, 2))
        # return

        for suit in self.__suits:
            for key,value in self.__cardset.items():
                if(self.__deckType == DeckType.Card36 and value < 6):
                    continue
                self.cards.append(Card(key, suit, iterator, value))
                iterator += 1
        print (f'Колода заполнена {str(len(self.cards))} картами')
    
    def shuffleDeck(self):
        if(len(self.cards) == 0):
            print ('В колоде нет карт!')
            return
        random.shuffle(self.cards)
        print ('Колода перемешана')