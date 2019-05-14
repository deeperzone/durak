from baseGame import BaseGame
from deck import DeckType
import random

class Durak(BaseGame):
    def defineTrump(self):
        cardNumber = random.randint(0, len(self._deck.cards) - 1)
        self.trumpCard = self._deck.cards.pop(cardNumber)
        print(f'Козырная карта в колоде: {self.trumpCard.fullName()}')
    
  #  def defineFirstMove:
        

durak = Durak(['Иван', 'bot'], DeckType.Card36, 6)
durak.fillDeck()
durak.shuffleDeck()
durak.handOverCards()
durak.defineTrump()