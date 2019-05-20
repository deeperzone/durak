from console import print_

class Move:
    def __init__(self, trumpCard, playerMove, playerDefense):
        self.trumpCard = trumpCard
        self.playerMove = playerMove
        self.playerDefense = playerDefense
        self.isOver = False
        self.cards = []

    def moveOver(self):
        self.isOver = True

    def print_Move(self, player, isMove):
        if(player.isBot):
            s = ''
            for x in range(0, len(self.cards)):
                if(x == 0 or x % 2 == 0):
                    separator = '' if x == 0 else '\n'
                    s+= f'{separator}{str(int(x/2 + 1))}) {self.playerMove.name} Ходит '
                else:
                    s+= f' -> {self.playerDefense.name} Отбивает '
                s+= self.cards[x].fullName()
            print_ (s, startWith='\n', endWith='\n')
        if(player is not None and self.isOver):
            if(isMove):
                print_(f'\033[42mИгрок {player.name} завершил ход\033[00m', startWith='\n', endWith='\n')
            else:
                print_(f'\033[41mИгрок {player.name} взял(-а) карты\033[00m', startWith='\n', endWith='\n')

    def add(self, player, card):
        if(self.__checkMoveCard(card) == False):
            return False
        self.cards.append(card)

        if(len(self.cards) == 12): 
            self.isOver = True
        return True

    def __checkMoveCard(self, card):
        return True