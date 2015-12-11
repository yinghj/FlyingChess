# Huiji Ying & Yuhao Wan
# CS111, Carleton College
# Flying Chess, Final Project
# player.py

# a chunk of code to create the players of the game.
from chess import *
from die import *
from board import *

class Player:
    def __init__(self, name, board):
        # A player class needs to record the player's name, 
        # the number of chess pieces he has in play, 
        # all the information about the chesses he owns, 
        # the number he gets from throwing a die,
        # and the piece of chess he/she is moving.
        self.name = name
        self.piece = 4
        self.board = board
        self.chess = [Chess(1),Chess(2),Chess(3),Chess(4)]
        self.die = 0
        self.currentC = ''

        
    def getName(self): return self.name
    def getPieceNum(self): return self.piece

    
    # Below is part of the computer stragety when making a move in normal circumstances.
    def chooseChess(self, num):
        chessNum = 0
        maxValue = 0
        for currNum in self.chess:
            # If there are chesses in the airport and the die gets a 6, move the chess
            # out of the airport first. Assign each chess with the top priority value.
            if currNum.position == 'airport' and num == 6:
                currNum.value = 100
            # Move the leading chess if there are no special circumstances.
            # Assign chess value according to its position.
            elif currNum.position != 'airport' and currNum.status:
                if currNum.value < 57:
                    currNum.value = currNum.position + 10
        # Move the chess containing the greatest value
        for che in self.chess:
            if che.value > maxValue:
                chessNum = che.num
                maxValue = che.value
        # The chess number is returned if there are chesses avaiable for moving.
        # If none, 0 is returned.
        return chessNum
    
    
    # A player makes a move by choosing a chess and update its position according to the 
    # die number he/she throws.
    def makeAmove(self, num):
        self.die = num
        print "Die Number >>>", self.die, " ",
        next = raw_input("Hit enter to continue")
        chessNum = self.chooseChess(self.die)
        position = ''
        # A move can be made only when there are available chesses in play.
        if chessNum:
            self.currentC = self.chess[chessNum-1]
            # If a human player accidentally choose a chess that is out of play,
            # ask him to choose again. But if the human player choose a chess at 
            # the airport but he doesn't get the 6 on this move, it will be counted
            # as a violation and he can't make the move in this round.
            while not self.currentC.status:
                chessNum = self.chooseChess(self.die)
                self.currentC = self.chess[chessNum-1]
            position = self.currentC.updatePosition(self.die)
            # If a chess reaches the finishline after the move is made,
            # update the number of chess-piece of the player.
            if not self.currentC.status:
                self.piece = self.piece - 1
            # If a player gets a 6 from the die, he can throw the die again
            # and make one more move.
            return self.currentC.position

# Human players has different functions from those of the computer player.
class HumanPlayer(Player):
    # How a human player chooses the chess he wants to move.
    def chooseChess(self,num):
        # If there are chesses moveable on the game board, ask the human player to 
        # choose the number of chess-piece he wants to move.
        if self.moveable(num): 
            self.board.chosenChess = ''
            next = raw_input("Please click on the chess you want to move, then press enter to continue")
            chess = self.board.chosenChess
            while chess == '' or (not chess.newClicks >= chess.clicks + 1):
                next = raw_input("Please click on the chess you want to move, then press enter to continue")
                chess = self.board.chosenChess

            chess.clicks = chess.newClicks
            chessNum = chess.buttonNum
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
    die = DieRoll(15, 565, 169, 167,'Roll')
    y1 = ChessButton('yellow', Point(609,610),1)
    y2 = ChessButton('yellow', Point(685,610),2)
    y3 = ChessButton('yellow', Point(609,685),3)
    y4 = ChessButton('yellow', Point(685,685),4)
    g1 = ChessCom('green', Point(65,64),1)
    g2 = ChessCom('green', Point(141,64),2)
    g3 = ChessCom('green', Point(65,136),3)
    g4 = ChessCom('green', Point(141,136),4)
    buttons = [y1,y2,y3,y4]
    computerChesses = [g1,g2,g3,g4]
    win = Board('Flying Chess', 750, 750, buttons, computerChesses)
    for button in buttons:
        button.draw(win)
    for chess in computerChesses:
        chess.draw(win)
    die.draw(win)

    a = HumanPlayer('a',win)
    for n in range(15):
        a.makeAmove()
        for i in a.chess:
            print i.position
    while not win.closed():
        win.update()  
    

