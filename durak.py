from baseGame import BaseGame
from deck import DeckType
from player import Player
from move import Move
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
        return playerFirstMove

    def nextPlayer(self, currentPlayer):        
        index = self._players.index(currentPlayer) + 1
        if(index > len(self._players) - 1):
            return self._players[0]
        else:
            return self._players[index]

    # def checkLoser(self):
    #     playersWithCard = []
    #     for player in self._players:
    #         if(len(player.cards) > 0):
    #             playersWithCard.append(player)
    #     if(len(playersWithCard) == 1): return playersWithCard[0]
    #     else: return None


durak = Durak([Player('Иван'), Player('bot', True)], DeckType.Card36, 6)
durak.fillDeck()
durak.shuffleDeck()
durak.handOverCards()
durak.defineTrump()
playerMove = durak.defineFirstMovePlayer()

while (input('Enter: ')!= 'exit'):
    playerDefense = durak.nextPlayer(playerMove)
    print (f'Игрок: {playerMove.name} ходит, Игрок: {playerDefense.name} отбивается')
    move = Move(durak.trumpCard, playerMove, playerDefense)

    while(move.isOver == False):
        playerMove.setCurrentMove(move)
        playerDefense.setCurrentMove(move)        
    # card = player.getCurrentMoveCard(durak.trumpCard)
    # move = Move(durak.trumpCard)
    # move.add(card)
