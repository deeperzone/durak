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

    def setCurrentMove(self, move):
        if(move.playerMove == self):
            self.__move(move)
        else:
            self.__defense(move)

    def __defense(self, move):
        # Пока кидаем первую карту
        if(self.isBot):
            move.add(self, self.cards.pop(0))
            print (f'{move.playerDefense.name} думает...')
        else: self.__userInput(move, False)

    def __move(self, move):
        if(self.isBot):
            card = self.__aiFindCard(move)
            move.add(self, card)
            self.cards.remove(card)
        else: self.__userInput(move, True)

    def __checkAvailable(self, move, card):
        if(card is None): 
            return False
        if(len(move.cards) == 0): 
            return True
        # Если ходим
        if(move.playerMove == self):
            return any(x.name == card.name for x in move.cards)
        # Если отбиваемся
        return True

    def __userInput(self, move, isMove):
        currentActionName = 'Ходите' if isMove else 'Отбивайтесь'
        print (f'########## {self.name} -> {currentActionName}, выберите карту: ##########')
        while (True):
            cardNumber = input(Card.showCards(self.cards)+': ')
            card = self.__findCard(cardNumber)
            if(self.__checkAvailable(move, card) and move.add(self, card)):
                self.cards.remove(card)
                return
            else: print ('Не допустимый ход')

    def __findCard(self, cardNumber):
        try:
            cardNumber = int(cardNumber)
        except ValueError:
            return None

        for i in range(0, len(self.cards)):
            if(self.cards[i].number == cardNumber):
                return self.cards[i]
        return None

    def __aiFindCard(self, move):
        minCard = self.__aiGetMin(move, False)
        if(minCard == None): minCard = self.__aiGetMin(move, True)
        return minCard

    def __aiGetMin(self, move, isTrump):
        cards = list(filter(lambda x: (x.suit == move.trumpCard.suit) == isTrump, self.cards))
        if(len(cards) == 0): return None
        return min(cards, key=lambda x: x.number)

        

