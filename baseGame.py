from deck import Deck, DeckType
from player import Player
import random

class BaseGame: 
    def __init__(self, players, deckType, cardsInHand):
        if(type(deckType) != DeckType): raise Exception('Не удалось определить колоду')
        self._players = players
        self._deck = Deck(deckType)
        self._cardsInHand = cardsInHand

    def fillDeck(self):
        self._deck.fillDeck()

    def shuffleDeck(self):
        self._deck.shuffleDeck()

    def handOverCards(self):
        for player in self._players:
            player.handOverCards(self._deck, self._cardsInHand)