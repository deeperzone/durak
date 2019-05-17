class Move:
    def __init__(self, trumpCard, playerMove, playerDefense):
        self.trumpCard = trumpCard
        self.playerMove = playerMove
        self.playerDefense = playerDefense
        self.isOver = False
        self.cards = []

    def moveOver(self):
        self.isOver = True

    def toStr(self):
        s = ''
        for x in range(0, len(self.cards)):
            if(x == 0 or x % 2 == 0): 
                s+= f'\n {str(int(x/2 + 1))}) {self.playerMove.name} Ходит '
            else:
                s+= f' -> {self.playerDefense.name} Отбивает '
            s+= self.cards[x].fullName()
        s+='\n'
        return s

    def add(self, player, card):
        if(self.__checkMoveCard(card) == False):
            return False
        self.cards.append(card)

        if(len(self.cards) == 12): 
            self.isOver = True
        return True

    def __checkMoveCard(self, card):
        return True