# Huiji Ying & Yuhao Wan
# CS111, Carleton College
# Flying Chess, Final Project
# system.py

# a chunk of code to create the system of the game.
from chess import *
from die import *
from player import *
from board import *


class System:
    def __init__(self, board):
        # The system contains all information about the players, the map of the board,
        # and announcement of the final winner.
        self.winner = ''
        # This creates a list of players: computer and human player
        self.player = [Player('Computer',board), \
                       HumanPlayer('PLAYER '+raw_input('Please enter your name:'),board)]
        # This maps out each position a chess can go on the board
        self.map = [[ 1, 2, 3, 4, 5, 6, 7, 8, 9,10,\
                     11,12,13,14,15,16,17,18,19,20,\
                     21,22,23,24,25,26,'','','','',\
                     '','',27,28,29,30,31,32,33,34,\
                     35,36,37,38,39,40,41,42,43,44,\
                     45,46,47,48,49,50,'','',51,52,\
                     53,54,55,56,'','','','airport','the end',0],\
                    [27,28,29,30,31,32,33,34,35,36,\
                     37,38,39,40,41,42,43,44,45,46,\
                     47,48,49,50,'','',51,52,53,54,\
                     55,56, 1, 2, 3, 4, 5, 6, 7, 8,\
                      9,10,11,12,13,14,15,16,17,18,\
                     19,20,21,22,23,24,25,26,'','',\
                     '','','','','airport','the end',0,'','','']]
        self.board = board
        self.currentMove = ''
        self.computerChessValue = [0,0,0,0]
       
    def updateBoard(self, newbuttons, newchesses):
        self.board.buttons = newbuttons
        self.board.computerChesses = newchesses

    # Game begins.        
    def gameStart(self):
        # Human player goes first.
        currentP, opponent = self.player[1], self.player[0]
        while True:
            num = die.rollDie()
            # Below is part of the computer stragety when making a move, considering opponent's move.
            if currentP == self.player[0]:
                playerPosition = []
                for che in opponent.chess:
                    playerPosition.append(che.position)
                # If any of the computer chesses could catch the player's chesses, make that move
                # Assign that chess with second priority value.
                for che in currentP.chess:
                    che.value = 0
                    for i in range(len(playerPosition)):
                        if type(che.position) != type('airport'):
                            if che.position + num < 51:
                                if self.map[0].index(che.position + num) == self.map[1].index(playerPosition[i]) and (che.position + num) % 4 !=2:
                                    che.value = 90
                # If any of the computer chesses can take a shortcut, make that move
                # Assign that chess with third priority value.
                for che in currentP.chess:
                    if type(che.position) != type('airport'):
                        if (che.position + num) % 4 ==2 and (che.position + num) < 47:
                            che.value = 80
            self.currentMove = currentP.makeAmove(num)
            if self.currentMove or self.currentMove == 0:
                if currentP == self.player[1]:
                    self.board.movePlayerChess(self.currentMove)
                else:
                    self.board.moveComputerChess(self.currentMove, currentP.currentC.num)
              
            # Check if this player's moved chess has caught any of the oppenent's chess.
            if currentP.currentC != '':
                self.fight(currentP,opponent)
            # If die number is six, roll the die again
            while currentP.die == 6 and currentP.piece != 0:
                num = die.rollDie()
                if currentP == self.player[0]:
                    playerPosition = []
                    for che in opponent.chess:
                        playerPosition.append(che.position)
                    for che in currentP.chess:
                        che.value = 0
                        for i in range(len(playerPosition)):
                            if type(che.position) != type('airport'):
                                if che.position + num < 51:
                                    if self.map[0].index(che.position + num) == self.map[1].index(playerPosition[i]) and (che.position + num) % 4 !=2 :
                                        che.value = 90
                    for che in currentP.chess:
                        if type(che.position) != type('airport'):
                            if (che.position + num) % 4 == 2 and (che.position + num) < 47:
                                che.value = 80
                self.currentMove = currentP.makeAmove(num)
                if currentP == self.player[1]:
                    self.board.movePlayerChess(self.currentMove)
                else:
                    self.board.moveComputerChess(self.currentMove, currentP.currentC.num)
                if currentP.currentC != '':
                    self.fight(currentP,opponent)
            print currentP.getName(), 'has', currentP.piece, 'pieces of chess:' 
            # If the player's chesses has all reached the finishline after this move,
            # the player wins the game
            if currentP.piece == 0:
                self.winner = currentP.getName()
                break
            print currentP.getName(), ", your chesses are at", 
            for i in currentP.chess:
                print '[',i.position,']',
            print "\n", opponent.getName(), ", your chesses are at",
            for i in opponent.chess:
                print '[',i.position,']',
            print "\n","---------------------------------------------------------------------------"
            # Two players take turns in this game.
            currentP, opponent = opponent, currentP
            print "Current Player:", currentP.getName()
           
        if self.winner != '' and self.winner!= 'Computer':
            print "Congratulations,", self.winner, "! You win the game!"
        else:
            print "Sorry, you lose."
        
    # Each player has a different starting point on the board, but they share the same
    # route. But when their chesses reach the same point on the route, the chess arriving
    # at the point first gets caught. The point of the route and its corresponding position 
    # are shown on the map above.
    def fight(self,currentP,opponent):
        for chess in opponent.chess:
            # Check if two chesses are at the same point.
            # Use the position of each chess to retrieve its index which represents the
            # point of the route from the map above.
            if self.map[0].index(currentP.currentC.position)\
                == self.map[1].index(chess.position):
                chess.getCaught()
                self.currentMove = 'airport'
                chessNum = chess.num
                print opponent.getName(), ', your chess No.', chess.getNum(), \
                'is sent back to the airport.'
                if opponent == self.player[1]:
                    self.board.chosenChess = self.board.buttons[chessNum-1]
                    self.board.movePlayerChess(self.currentMove)
                else:
                    self.board.moveComputerChess(self.currentMove, chessNum)



buttons = []
computerChesses =[]
win = Board('Flying Chess', 750, 750, buttons, computerChesses)
system = System(win) 
die = DieRoll(15, 565, 169, 167,'Roll')
y1 = ChessButton('yellow', Point(609,610),1,system)
y2 = ChessButton('yellow', Point(685,610),2,system)
y3 = ChessButton('yellow', Point(609,685),3,system)
y4 = ChessButton('yellow', Point(685,685),4,system)
g1 = ChessCom('green', Point(65,64),1,system)
g2 = ChessCom('green', Point(141,64),2,system)
g3 = ChessCom('green', Point(65,136),3,system)
g4 = ChessCom('green', Point(141,136),4,system)
buttons = [y1,y2,y3,y4]
computerChesses = [g1,g2,g3,g4]
system.updateBoard(buttons, computerChesses)

    
for button in buttons:
    button.draw(win)
for chess in computerChesses:
    chess.draw(win)
die.draw(win)

               
system.gameStart()   

while not win.closed():
    win.update()  
