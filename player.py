from card import Card

class Player:
    def __init__(self, name, isBot = False):
        self.name = name
        self.isBot = isBot
    
    def handOverCards(self, deck, count):
        if(len(deck.cards) == 0):
            print ('В колоде нет карт!')
            return
        self.cards = []
        destLength = count - len(self.cards)
        iterator = 0
        if(destLength <= 0):
            print (f'Игроку {self.name} не нужны карты')
            return
        while (iterator != destLength):
            self.cards.append(deck.cards.pop())
            iterator += 1
        print (f'Игрок {self.name} взял {str(destLength)} карт')

    def setCurrentMove(self):
        if(self.isBot):
            return
        print (f'########## {self.name} -> Ваш ход, выберите карту: ##########')
        card = None
        while (card == None):
            cardNumber = input(Card.showCards(self.cards)+': ')
            card = self._findCardIndex(cardNumber)
        return card

    def _findCardIndex(self, cardNumber):
        try:
            cardNumber = int(cardNumber)
        except ValueError:
            return None

        for card in self.cards:
            if(card.number == cardNumber):
                return card
        return None

    def _aiFindCard(self):
        pass
        

