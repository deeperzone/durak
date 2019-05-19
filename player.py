from card import Card

class Player:
    def __init__(self, name, isBot = False):
        self.name = name
        self.isBot = isBot
        self.cards = []
    
    def handOverCards(self, deck, count):
        self.cards = sorted(self.cards, key=lambda x: x.value)
        if(len(deck.cards) == 0):
            print ('В колоде нет карт!')
            return
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
        if(move.isOver):
            return
        if(move.playerMove == self):
            self.__move(move)
        else:
            self.__defense(move)
        print(move.toStr())

    def __defense(self, move):
        if(move.isOver == True):
            return
        print (f'{move.playerDefense.name} думает...')
        # Пока кидаем первую карту
        if(self.isBot):
            for card in self.__aiGetCards():
                if(self.__checkAvailable(move, card)):
                    self.cards.remove(card)
                    move.add(self, card)
                    return
            self.__getCards(move)
            self.__moveOver(move)
        else: self.__userInput(move, False)

    def __move(self, move):
        if(self.isBot):
            for card in self.__aiGetCards(): 
                if(self.__checkAvailable(move, card)):
                    move.add(self, card)
                    self.cards.remove(card)
                    return
            move.moveOver()
        else: self.__userInput(move, True)

    def __checkAvailable(self, move, moveCard):
        if(moveCard is None): 
            return False
        if(len(move.cards) == 0): 
            return True
        # Если ходим
        if(move.playerMove == self):
            return any(x.name == moveCard.name for x in move.cards)
        # Если отбиваемся
        cardForDefense = move.cards[len(move.cards)-1]
        # Ищем старшую карту той же масти
        if(moveCard.suit == cardForDefense.suit and moveCard.value > cardForDefense.value):
            return True
        if(move.trumpCard.suit != cardForDefense.suit and move.trumpCard.suit == moveCard.suit):
            return True
        return False

    def __getCards(self, move):
        move.moveOver()
        self.cards = self.cards + move.cards
        print (f'Игрок {self.name} взял карты')

    def __moveOver(self, move):
        move.moveOver()
        print (f'Игрок {self.name} завершил ход')

    def __userInput(self, move, isMove):
        currentActionName = 'Ходите' if isMove else 'Отбивайтесь'
        print (f'########## {self.name} -> {currentActionName}, выберите карту: ##########')
        if(isMove): 
            print ('########## Для завершения хода введите: end')
        else:
            print ('########## Чтобы взять карты введите: get')
        while (True):
            cardNumber = input(Card.showCards(self.cards)+': ')
            if(isMove and cardNumber == 'end' and len(move.cards) > 1):
                self.__moveOver(move)
                return
            if(not isMove and cardNumber == 'get'):
                self.__getCards(move)
                return
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

    def __aiGetMin(self, move, isTrump):
        cards = list(filter(lambda x: (x.suit == move.trumpCard.suit) == isTrump, self.cards))
        if(len(cards) == 0): return None
        return min(cards, key=lambda x: x.number)

    def __aiGetCards(self):
        return sorted(self.cards, key=lambda x: x.value)

        

