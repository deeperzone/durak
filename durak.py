from baseGame import BaseGame
from deck import DeckType
from player import Player
import random

class Durak(BaseGame):
    def __init__(self, players, deckType, cardsInHand):
        super(Durak, self).__init__(players, deckType, cardsInHand)
        self.trumpCard = None

    def defineTrump(self):
        cardNumber = random.randint(0, len(self._deck.cards) - 1)
        self.trumpCard = self._deck.cards.pop(cardNumber)
        print(f'Козырная карта в колоде: {self.trumpCard.fullName()}')
    
    def _defineFirstMovePlayer(self):
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
        return playerFirstMove

    def nextPlayer(self):
        try:
            self.currentPlayer
        except AttributeError:
            self.currentPlayer = self._defineFirstMovePlayer()
            return self.currentPlayer
        
        index = self._players.index(self.currentPlayer) + 1
        if(index > len(self._players) - 1):
            self.currentPlayer = self._players[0]
            return self.currentPlayer
        else:
            self.currentPlayer = self._players[index]
            return self.currentPlayer

    def checkLoser(self):
        playersWithCard = []
        for player in self._players:
            if(len(player.cards) > 0):
                playersWithCard.append(player)
        if(len(playersWithCard) == 1): return playersWithCard[0]
        else: return None


durak = Durak([Player('Иван'), Player('bot', True)], DeckType.Card36, 6)
durak.fillDeck()
durak.shuffleDeck()
durak.handOverCards()
durak.defineTrump()

loser = None
while (loser == None):
    player = durak.nextPlayer()
    cardName = player.setCurrentMove(durak.trumpCard).fullName()
    print (f'Игрок {player.name} ходит: {cardName}')
    loser = durak.checkLoser()

print (f'Игрок {loser.name} проиграл')