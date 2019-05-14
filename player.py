class Player:
    def __init__(self, name):
        self.name = name
    
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
