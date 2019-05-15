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

    def setCurrentMove(self, trumpCard):
        cardIndex = None
        if(self.isBot):
            # print(Card.showCards(self.cards))
            cardIndex = self._aiFindCardIndex(trumpCard)
        else:
            print (f'########## {self.name} -> Ваш ход, выберите карту: ##########')
            while (cardIndex == None):
                cardNumber = input(Card.showCards(self.cards)+': ')
                cardIndex = self._findCardIndex(cardNumber)
        return self.cards.pop(cardIndex)

    def _findCardIndex(self, cardNumber):
        try:
            cardNumber = int(cardNumber)
        except ValueError:
            return None

        for i in range(0, len(self.cards)):
            if(self.cards[i].number == cardNumber):
                return i
        return None

    def _aiFindCardIndex(self, trumpCard):
        minCardIndex = self._aiGetMinIndex(trumpCard, False)
        if(minCardIndex == None): minCardIndex = self._aiGetMinIndex(trumpCard, True)
        return minCardIndex

    def _aiGetMinIndex(self, trumpCard, isTrump):
        cards = list(filter(lambda x: (x.suit == trumpCard.suit) == isTrump, self.cards))
        if(len(cards) == 0): return None
        return self.cards.index(min(cards, key=lambda x: x.number))

        

