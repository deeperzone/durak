from deck import Deck, DeckType
from player import Player

class Game: 
    def __init__(self, players, deckType):
        if(type(deckType) != DeckType): raise Exception('Не удалось определить колоду')
        self.players = players
        self.deck = Deck(deckType)

    def start(self):
        # Заполнить колоду картами
        self.deck.fillCards()
        # Перемешать колоду карт
        self.deck.shuffleDeck()
        print('Игра начата!')

game = Game([Player('Иван'), Player('bot')], DeckType.Card36)
game.start()