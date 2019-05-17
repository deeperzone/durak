class Card:
    def __init__(self, name, suit, number, value):
        self.name = name
        self.suit = suit
        self.number = number
        self.value = value

    def fullName(self):
        return f'{self.suit} {self.name}'

    @staticmethod
    def showCards(cards):
        cardStr = ''
        for card in cards:
            cardStr += f'{card.number}.[{card.fullName()}], '
        return cardStr.rstrip(' ').rstrip(',')
    