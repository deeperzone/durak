class Move:
    def __init__(self, trumpCard, playerMove, playerDefense):
        self.trumpCard = trumpCard
        self.playerMove = playerMove
        self.playerDefense = playerDefense
        self.isOver = False
        self.cards = []

    def moveOver(self):
        self.isOver = True

    def add(self, player, card):
        if(self.__checkMoveCard(card) == False):
            return False
        self.cards.append(card)

        if(len(self.cards) % 2 == 0):
            print (f'Игрок {player.name} отбил: {card.fullName()}')
        else:
            print (f'Игрок {player.name} подкинули: {card.fullName()}')

        if(len(self.cards) == 12): 
            self.isOver = True
        return True

    def __checkMoveCard(self, card):
        return True