import random

##### Константы
SUITS = ['♦','♥','♣','♠']
CARDSET = {'6': 6,'7': 7,'8': 8,'9': 9,'10': 10,'В': 11,'Д': 12,'К': 13,'Т': 14}
###############

class Card:
    def __init__(self, name, level, number):
        self.name = name
        self.level = level
        self.number = number

    def setSuit(self, suit):
        self.suit = suit
        if(suit.isTrump):
            self.level = self.level + 100

    def cardName(self):
        additional = '*' if self.suit.isTrump else ''
        return f'{str(self.number)}) {additional}{self.suit.name}{additional} {self.name}'

class Suit:
    def __init__(self, name, isTrump):
        self.name = name
        self.isTrump = isTrump

    @staticmethod
    def getSuits(setTrump):
        suits = []
        for suit in SUITS:
            suits.append(Suit(suit, False))
        if(setTrump):
            index = random.randint(0, len(SUITS) - 1)
            suits[index].isTrump = True
        return suits

class Player:
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck
        self.cards = []

    def fillHand(self, withLog):
        length = len(self.cards)
        if(length >= 6):
            print('У вас уже имеется необходимое кол-во карт!')
            return
        else:
            print(f'Берём {str(6 - length)} карт')

        while (len(self.cards) < 6):
            card = self.deck.pop()
            self.cards.append(card)
            if(withLog == True):
                print('Игрок ' + self.name + ' взял карту ' + card.cardName())

def fillCards(suits):
    deck = []
    iterator = 1
    for i in range(4):
        for key, value in CARDSET.items():
            newCard = Card(key, value, iterator)
            newCard.setSuit(suits[i])
            deck.append(newCard)
            iterator = iterator + 1
    return deck

def shuffleCards(deck):
    random.shuffle(deck)
    return deck

def showCards(cards):
    cardStr = ''
    for card in cards:
        cardStr = cardStr + card.cardName() + ' | '
    print(cardStr)

# Масти колоды, с определенным козырем (опция)
suits = Suit.getSuits(True)
# Колода карт
deck = fillCards(suits)
# Перемешать колоду карт
deck = shuffleCards(deck)

player = Player('Иван', deck)
bot = Player('Bot', deck)

def processCommand(command):
    lowerCmd = str.lower(command)
    if(lowerCmd == 'сдать'): player.fillHand(True)

readStr = input('Введите команду: ')
while (readStr != 'exit'):
    processCommand(readStr)
    readStr = input('Введите команду: ')

