# Huiji Ying & Yuhao Wan
# CS111, Carleton College
# Flying Chess, Final Project
# player.py  Text Version

# a chunk of code to create the players of the game.
from chess import *
from die import *


class Player:
    def __init__(self, name, color):
        # A player class need to record the player's name, 
        # the number of chess pieces he has in play, 
        # all the information about the chesses he owns, 
        # the number he gets from throwing a die,
        # and the piece of chess he is moving.
        self.name = name
        self.piece = 4
        self.color = color
        self.chess = [Chess(1),Chess(2),Chess(3),Chess(4)]
        self.die = 0
        self.currentC = ''

        
    def getName(self): return self.name
    def getPieceNum(self): return self.piece

    # Get a number from throwing the die.
    def roll(self): 
        self.die = ran()
        return self.die
    
    # How computer chooses the chess it wants to move.
    def chooseChess(self, num):
        chessNum = 0
        frontPosition = 0
        for currNum in self.chess:
            # If there are chesses in the airport and the die gets a 6, move the chess
            # out of the airport first.
            if currNum.position == 'airport' and num == 6:
                return currNum.num
            # If no chesses are available in the airport, move the leading chess.
            elif currNum.position != 'airport' and currNum.status:
                if currNum.position >= frontPosition:
                    frontPosition = currNum.position
                    chessNum = currNum.num
        # The chess number is returned if there are chesses avaiable for moving.
        # If none, 0 is returned.
        return chessNum
    
    
    # A player makes a move by choosing a chess and update its position according to the 
    # die number he throws.
    def makeAmove(self):
        num = self.roll()
        chessNum = self.chooseChess(num)
        position = ''
        # A move can be made only when there are available chesses in play.
        if chessNum:
            self.currentC = self.chess[chessNum-1]
            # If a human player accidentally choose a chess that is out of play,
            # ask him to choose again. But if the human player choose a chess at 
            # the airport but he doesn't get the 6 on this move, it will be counted
            # as a violation and he can't make the move in this round.
            while not self.currentC.status:
                chessNum = self.chooseChess(num)
                self.currentC = self.chess[chessNum-1]
            position = self.currentC.updatePosition(num)
            # If a chess reaches the finishline after the move is made,
            # update the number of chess-piece of the player.
            if not self.currentC.status:
                self.piece = self.piece - 1
            # If a player gets a 6 from the die, he can throw the die again
            # and make one more move.
            if num == 6:
                self.makeAmove()
        return position

# Human players has different functions from those of the computer player.
class HumanPlayer(Player):
    # How a human player chooses the chess he wants to move.
    def chooseChess(self,num):
        # If there are chesses moveable on the game board, ask the human player to 
        # choose the number of chess-piece he wants to move.
        if self.moveable(num):
            inNum = raw_input("Please enter the number of the chess you want move:")
            # Only number 1 to 4 are accepted.
            while inNum != '1' and inNum!= '2' and inNum != '3' and inNum != '4':
                inNum = raw_input("Please enter an integer between 1 and 4:")
            chessNum = int(inNum)
            return chessNum
        return 0
    # Automatically help the human player check if there are moveable chesses on the board.
    # Avoid asking player to make a choice every time after throwing the die.
    def moveable(self, num):
        # A player can't move when the chesses are all in airport and he doesn't get a 6.
        if num != 6:
            for chess in self.chess:
                if chess.position != 'airport' and chess.status:
                    return True
            return False
        else: 
            return True


if __name__ == '__main__':    
    a = Player('a', 'b')
    for n in range(15):
        a.makeAmove()
        for i in a.chess:
            print i.position
    

