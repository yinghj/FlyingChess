# Huiji Ying & Yuhao Wan
# CS111, Carleton College
# Flying Chess, Final Project
# chess.py

# a chunk of codes to create the chess component of the game.
class Chess:
    def __init__(self, num):
        # A chess contains the information of its number, its current position,
        # and whether it is playable.
        self.num = num
        self.position = 'airport'
        self.status = 1

        
    def getNum(self): return self.num
    def getPosition(self): return self.position
    
    # Update the position of the chess when a move is made.
    def updatePosition(self, dieNum): 
        # A chess can move forward only when it is playable but not in the airport.
        if self.status and self.position != 'airport':
            self.position = self.position + dieNum
            # If a chess reaches the finishline, it is out of the game.
            if self.position >= 56:
                self.finish()
            # If a chess is playable, it can have shortcut moves when reaching certain
            # positions as described below.
            if self.status:
                if self.position % 4 == 2 and self.position < 50 and self.position != 18:
                    self.position += 4
                elif self.position == 18:
                    self.position == 30            
        # A chess can move out of the airport when the player gets a 6.    
        elif dieNum == 6 and self.position == 'airport':
            self.takeoff()
        return self.position
    
    # Move the chess to a position ready for further movements.
    def takeoff(self):
        self.position = 0
    
    # A chess can be sent back to the airport if it is caught by its opponent's chess.    
    def getCaught(self):
        self.position = 'airport'
    
    # Take the chess out of the game if it reaches the finishline.
    def finish(self):
        self.status = 0
        self.position = 'the end'