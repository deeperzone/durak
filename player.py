from card import Card

class Player:
    GETTEXT = 'беру'
    PASSTEXT = 'бита'

    def __init__(self, name, isBot = False):
        self.name = name
        self.isBot = isBot
        self.cards = []

    def handOverCards(self, deck, count):
        if(len(deck.cards) == 0):
            print ('В колоде нет карт!')
            return
        destLength = count - len(self.cards)
        iterator = 0
        if(destLength <= 0):
            print (f'Игроку {self.name} не нужны карты')
            return
        while (iterator != destLength and len(deck.cards) != 0):
            self.cards.append(deck.cards.pop())
            iterator += 1
        print (f'Игрок {self.name} взял(-а) {str(destLength)} карт')

    def setCurrentMove(self, move):
        self.cards = sorted(self.cards, key=lambda x: x.value)
        if(move.isOver):
            return
        if(move.playerMove == self):
            self.__move(move)
            if(self.isBot and not move.isOver):
                print(move.toStr(self, True))
        else:
            self.__defense(move)
            if(self.isBot):
                print(move.toStr(self, False))

    def __defense(self, move):
        if(move.isOver == True):
            return
        if(self.isBot):
            for card in self.__aiGetCards():
                if(self.__checkAvailable(move, card)):
                    self.cards.remove(card)
                    move.add(self, card)
                    return
            self.__getCards(move)
        else: 
            self.__userInput(move, False)

    def __move(self, move):
        if(self.isBot):
            for card in self.__aiGetCards(): 
                if(card.suit == move.trumpCard.suit and len(move.cards) > 0):
                    continue
                if(self.__checkAvailable(move, card)):
                    move.add(self, card)
                    self.cards.remove(card)
                    return
            self.__moveOver(move)
        else: 
            self.__userInput(move, True)

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

    def __moveOver(self, move):
        move.moveOver()

    def __userInput(self, move, isMove):
        currentActionName = f'\033[92mВаш ход, {self.name}\033[00m' if isMove else f'\033[91mОтбивайтесь, {self.name}\033[00m'
        if(isMove and len(move.cards) > 0): 
            print (f'########## Для завершения хода введите команду: \033[95m{self.PASSTEXT}\033[00m')
        elif(not isMove):
            print (f'########## Чтобы взять карты введите команду: \033[95m{self.GETTEXT}\033[00m')
        print (f'########## Козырная карта: {move.trumpCard.fullName()}')
        print (f'########## {currentActionName}. Введите номер карты ##########')
        while (True):
            Card.showCards(self.cards)
            cardNumber = input(': ')
            if(isMove and cardNumber == self.PASSTEXT and len(move.cards) > 1):
                self.__moveOver(move)
                return
            if(not isMove and cardNumber == self.GETTEXT):
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

        

