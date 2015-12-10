# Huiji Ying & Yuhao Wan
# CS111, Carleton College
# Flying Chess, Final Project
# system.py

# a chunk of code to create the system of the game.
from chess import *
from die import *
from player import *


class System:
    def __init__(self):
        # The system contains all information about the players
        # and announcement of the final winner.
        self.winner = ''
        self.player = [Player('Computer','blue'), \
                       HumanPlayer(raw_input('Please enter your name:'),'red')]
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
        
     
    # Game begins.        
    def gameStart(self):
        # Human player goes first.
        currentP, opponent = self.player[1], self.player[0]
        while True:
            currentP.makeAmove()
            # Check if this player's moved chess has caught any of the oppenent's chess.
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
            print "\n--------------------------------------------------"
            # Two players take turns in this game.
            currentP, opponent = opponent, currentP
            print "Current Player:", currentP.getName()
           
        if self.winner != '' and self.winner!= 'Computer':
            print "Congratulations,", self.winner, "! You win the game!"
        else:
            print "Sorry, you lose."
        
    # Each player has a different starting point, but they share the same
    # route. But when their chesses reach the same point on the route, the chess arriving
    # at the point first gets caught.
    def fight(self,currentP,opponent):
        for chess in opponent.chess:
            # Check if two chesses are at the same point.
            # Use the position of each chess to retrieve its index 
            if self.map[0].index(currentP.currentC.position)\
                == self.map[1].index(chess.position):
                chess.getCaught()
                print opponent.getName(), ', your chess No.', chess.getNum(), \
                'is sent back to the airport.'

if __name__ == '__main__':  
 
    a = System()                
    a.gameStart()   
