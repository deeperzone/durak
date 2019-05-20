from baseGame import BaseGame
from deck import DeckType
from player import Player
from move import Move
from os import system, name
from console import print_
import random

# define our clear function 
def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 
class Durak(BaseGame):
    def __init__(self, players, deckType, cardsInHand):
        super(Durak, self).__init__(players, deckType, cardsInHand)
        self.trumpCard = None

    def defineTrump(self):
        cardNumber = random.randint(0, len(self._deck.cards) - 1)
        self.trumpCard = self._deck.cards.pop(cardNumber)
        self._deck.cards.insert(0, self.trumpCard)
        for card in self._deck.cards:
            if(card.suit == self.trumpCard.suit):
                card.value += 100
        print_(f'Козырная карта в колоде: {self.trumpCard.fullName()}')
    
    def __defineFirstMovePlayer(self):
        if (self.trumpCard == None):
            print_ ('Козырь не определён!')
            return None
        minPlayerCard = {}
        for player in self._players:
            cards = filter(lambda x: x.suit == self.trumpCard.suit, player.cards)
            minCard = min(cards, key=lambda x: x.number, default=None)
            if(minCard is None): continue
            minPlayerCard[player] = minCard
        playerFirstMove = min(minPlayerCard.items(), key=lambda x: x[1].number, default=None)
        if(playerFirstMove is None):
            print_ ('У игроков нет козырей. Определяем случайным образом')
            index = random.randint(0, len(self._players)-1)
            playerFirstMove = self._players[index]
        else:
            playerFirstMove = playerFirstMove[0]
        return playerFirstMove

    def __nextPlayer(self):
        if(len(self._players) < 2):
            print_ ('Для игры необходимо минимум 2 игрока!')
            return  

        try:
            self.__currentPlayer
        except AttributeError:
            self.__currentPlayer = self.__defineFirstMovePlayer()
            return self.__currentPlayer

        if(self.__currentPlayer is None):
            print_ ('Не определен игрок, который ходит первым!')
            return    
        index = self._players.index(self.__currentPlayer) + 1
        if(index > len(self._players) - 1):
            return self._players[0]
        else:
            return self._players[index]

    def nextPlayers(self, move = None):
        if(move is not None and len(move.cards) % 2 != 0):
            self.__currentPlayer = self.__nextPlayer()
        self.__currentPlayer = self.__nextPlayer() 
        return (self.__currentPlayer, self.__nextPlayer())

    def checkLoserExist(self):
        playersWithCard = []
        for player in self._players:
            if(len(player.cards) > 0):
                playersWithCard.append(player)
        if(len(playersWithCard) == 1): 
            input (f'\033[44m\033[91mИгрок {playersWithCard[0].name} проиграл! Игра закончена.\033[00m')
            return True
        elif(len(playersWithCard) == 0):
            input ('\033[44m\033[91mИгроки сыграли в ничью!\033[00m')
            return True
        else: 
            return False

clear()
name = input('Введите имя игрока: ')
# TODO вернуть 6 карт
durak = Durak([Player(name), Player('bot', True)], DeckType.Card36, 6)
durak.fillDeck()
durak.shuffleDeck()
durak.defineTrump()
durak.handOverCards()
move = None
loser = None
while (not loser):
    players = durak.nextPlayers(move)
    playerMove = players[0]
    playerDefense = players[1]
    move = Move(durak.trumpCard, playerMove, playerDefense)

    while(move.isOver == False and not loser):
        playerMove.setCurrentMove(move)
        playerDefense.setCurrentMove(move)
        loser = durak.checkLoserExist()
    
    if(loser): break
    
    durak.handOverCards()