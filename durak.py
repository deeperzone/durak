from baseGame import BaseGame
from deck import DeckType
import random

class Durak(BaseGame):
    def __init__(self, players, deckType, cardsInHand):
        super(Durak, self).__init__(players, deckType, cardsInHand)
        self.trumpCard = None

    def defineTrump(self):
        cardNumber = random.randint(0, len(self._deck.cards) - 1)
        self.trumpCard = self._deck.cards.pop(cardNumber)
        print(f'Козырная карта в колоде: {self.trumpCard.fullName()}')
    
    def defineFirstMovePlayer(self):
        if (self.trumpCard == None):
            print ('Козырь не определён!')
            return
        minPlayerCard = {}
        for player in self._players:
            cards = filter(lambda x: x.suit == self.trumpCard.suit, player.cards)
            minCard = min(cards, key=lambda x: x.number, default=None)
            if(minCard is None): continue
            minPlayerCard[player] = minCard
        playerFirstMove = min(minPlayerCard.items(), key=lambda x: x[1].number, default=None)
        if(playerFirstMove is None):
            print ('У игроков нет козырей. Определяем случайным образом')
            index = random.randint(0, len(self._players)-1)
            playerFirstMove = self._players[index]
        else:
            playerFirstMove = playerFirstMove[0]
        print (f'Первый ход у игрока: {playerFirstMove.name}')


durak = Durak(['Иван', 'bot'], DeckType.Card36, 6)
durak.fillDeck()
durak.shuffleDeck()
durak.handOverCards()
durak.defineTrump()
durak.defineFirstMovePlayer()