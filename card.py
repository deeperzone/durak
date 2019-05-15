class Card:
    def __init__(self, name, suit, number):
        self.name = name
        self.suit = suit
        self.number = number

    def fullName(self):
        return f'{self.suit} {self.name}'

    @staticmethod
    def showCards(cards):
        cardStr = ''
        for card in cards:
            cardStr += f'{card.number}.[{card.fullName()}], '
        return cardStr.rstrip(' ').rstrip(',')
    