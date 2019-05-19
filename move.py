class Move:
    def __init__(self, trumpCard, playerMove, playerDefense):
        self.trumpCard = trumpCard
        self.playerMove = playerMove
        self.playerDefense = playerDefense
        self.isOver = False
        self.cards = []

    def moveOver(self):
        self.isOver = True

    def toStr(self, player, isMove):
        s = ''
        for x in range(0, len(self.cards)):
            if(x == 0 or x % 2 == 0):
                s+= f'\n{str(int(x/2 + 1))}) {self.playerMove.name} Ходит '
            else:
                s+= f' -> {self.playerDefense.name} Отбивает '
            s+= self.cards[x].fullName()
        if(player is not None and self.isOver):
            if(isMove):
                s+=f'\n\033[42mИгрок {player.name} завершил ход\033[00m'
            else:
                s+=f'\n\033[41mИгрок {player.name} взял(-а) карты\033[00m'
        return s+'\n'

    def add(self, player, card):
        if(self.__checkMoveCard(card) == False):
            return False
        self.cards.append(card)

        if(len(self.cards) == 12): 
            self.isOver = True
        return True

    def __checkMoveCard(self, card):
        return True