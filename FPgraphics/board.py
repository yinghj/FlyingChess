# Huiji Ying & Yuhao Wan
# CS111, Carleton College
# Flying Chess, Final Project
# board.py

# A chunk of code to create the game board. The following code has made use of and modified DLN's skeleton code buttons.py
from graphics import *
from die import *
from chess import *
from player import *



class Board:
    def __init__(self, title, width, height, buttons, computerChesses):
        # The board contains a window of the board and buttons of airport 
        # of which the chesses land on
        self.window = GraphWin(title, width, height)
        self.boardImage = Image(Point(width/2, height/2),'board.gif')
        self.boardImage.draw(self.window)
        self.window.setMouseHandler(self.handleClick)
        self.lastupdate = time.time()
        self.buttons = buttons
        self.computerChesses = computerChesses
        self.chosenChess =''
       
    def update(self):
        self.window.update()

    def closed(self):
        return not self.window.winfo_exists()        
    # Enables mouse-click of the buttons
    def handleClick(self, point):
        for button in self.buttons:
            if button.pointInside(point):
                self.chosenChess = button
                button.onClick()
    # Moves player's chesses
    def movePlayerChess(self,position):
        self.chosenChess.move(position)
    # Moves computer's chesses
    def moveComputerChess(self,position,chessnum):
        self.chosenChess = self.computerChesses[chessnum-1]
        self.chosenChess.move(position)
  
class ChessButton:
    # Chess buttons contains information of the number of the die
    # shows, the location of each position, and the destination
    # of the chess owned by the player
    def __init__(self, color, location, num, system):
        self.image = Image(location, color+'.gif')
        self.destination = location
        self.xRange = [self.destination.getX() - self.image.getWidth()/2,\
                       self.destination.getX() + self.image.getWidth()/2]
        self.yRange = [self.destination.getY() - self.image.getHeight()/2,\
                       self.destination.getY() + self.image.getHeight()/2,]

        self.clicks = 0
        self.newClicks = 0
        self.buttonNum = num
        # Maps out the player chesses' positions and destinations
        # and their corresponding points on the board
        self.map = [27,28,29,30,31,32,33,34,35,36,\
                     37,38,39,40,41,42,43,44,45,46,\
                     47,48,49,50,'','',51,52,53,54,\
                     55,56, 1, 2, 3, 4, 5, 6, 7, 8,\
                      9,10,11,12,13,14,15,16,17,18,\
                     19,20,21,22,23,24,25,26,'','',\
                     '','','','','airport','the end',0,'','','']
        self.destinations = [Point(70,245), Point(120,228), Point(162,228), Point(207,244), Point(242,213), Point(226,164), Point(226,122), Point(244,77), Point(290,60), Point(331,60),\
                            Point(373,60), Point(414,60), Point(456,60), Point(501,80), Point(520,125), Point(520,166),Point(501,216), Point(532,247), Point(584,230), Point(626,230),\
                            Point(675,248), Point(687,293), Point(687,334), Point(687,379),"","", Point(623,380), Point(580,380), Point(540,380), Point(498,380),\
                            Point(457,380), Point(415,380), Point(671,508), Point(624,522), Point(583,522), Point(536,506), Point(501,539), Point(520,585), Point(520,627), Point(504,674),\
                            Point(455,691), Point(414,690), Point(371,691), Point(331,690), Point(288,691), Point(242,677), Point(225,627), Point(226,586), Point(242,539), Point(207,509),\
                            Point(162,521), Point(120,522),Point(75,508), Point(57,508), Point(57,418), Point(57,375), Point(57,333), Point(57,292),"","",\
                            "","","","",location, Point(735,737), Point(708,536),"","",""]
        self.nextdestination = ''

    def draw(self, window):
        self.image.draw(window.window)
    # Set the paramenters of the mouse-click for the buttons    
    def pointInside(self, point):
        return self.xRange[0] <= point.getX() <= self.xRange[1] \
            and self.yRange[0] <= point.getY() <= self.yRange[1] \
    # Enables multiple clicks     
    def onClick(self):
        self.newClicks = self.clicks + 1
        return self.buttonNum
    # Moves the player chesses according to the mapped positions on thr board    
    def move(self, position):
        i = self.map.index(position)
        self.nextdestination = self.destinations[i]
        dx, dy =  self.nextdestination.getX() - self.destination.getX(), self.nextdestination.getY() - self.destination.getY()
        self.image.move(dx,dy)
        self.destination = self.nextdestination
        self.xRange = [self.destination.getX() - self.image.getWidth()/2,\
                        self.destination.getX() + self.image.getWidth()/2]
        self.yRange = [self.destination.getY() - self.image.getHeight()/2,\
                        self.destination.getY() + self.image.getHeight()/2,]


        
class ChessCom:
    # Computer chess buttons contains information of the number of the die
    # shows, the location of each position, and the destination
    # of the chess owned by the computer
    def __init__ (self, color, location, num, system):
        self.image = Image(location, color+'.gif')
        self.destination = location
        self.buttonNum = num
        # Maps out the positions and destintaions of the computer chesses
        # and their corresponding points on the board
        self.map = [ 1, 2, 3, 4, 5, 6, 7, 8, 9,10,\
                     11,12,13,14,15,16,17,18,19,20,\
                     21,22,23,24,25,26,'','','','',\
                     '','',27,28,29,30,31,32,33,34,\
                     35,36,37,38,39,40,41,42,43,44,\
                     45,46,47,48,49,50,'','',51,52,\
                     53,54,55,56,'','','','airport','the end',0]
        self.destinations = [Point(70,245), Point(120,228), Point(162,228), Point(207,244), Point(242,213), Point(226,164), Point(226,122), Point(244,77), Point(290,60), Point(331,60),\
                            Point(373,60), Point(414,60), Point(456,60), Point(501,80), Point(520,125), Point(520,166),Point(501,216), Point(532,247), Point(584,230), Point(626,230),\
                            Point(675,248), Point(687,293), Point(687,334), Point(687,379), Point(687,417), Point(687,459),  "" ,"","","",\
                            "","", Point(671,508), Point(624,522), Point(583,522), Point(536,506), Point(501,539), Point(520,585), Point(520,627), Point(504,674),\
                            Point(455,691), Point(414,690), Point(371,691), Point(331,690), Point(288,691), Point(242,677), Point(225,627), Point(226,586), Point(242,539), Point(207,509),\
                            Point(162,521), Point(120,522),Point(75,508), Point(57,508), Point(57,418), Point(57,375), "","", Point(122, 374),Point(164, 374),\
                            Point(205, 374),Point(247, 374), Point(288, 374),Point(330, 374),"","","",location, Point(7,6), Point(39,206)]
        self.nextdestination = ''
        self.newClicks = 0
        self.clicks = 0
        self.currentMove = system.currentMove
    # Draws the window
    def draw(self, window):
        self.image.draw(window.window)
    # Moves the computer's chesses accordingly    
    def move(self, position):
        i = self.map.index(position)
        self.nextdestination = self.destinations[i]
        dx, dy =  self.nextdestination.getX() - self.destination.getX(), self.nextdestination.getY() - self.destination.getY()
        self.image.move(dx,dy)
        self.destination = self.nextdestination
        

           
class DieRoll:
    def __init__(self, x, y, width, height, name):
        # Die roll contains the die showed on the lower-left corner on the board
        self.xRange = [x, x + width]
        self.yRange = [y, y + height]
        self.rectangle = Rectangle(Point(x, y), Point(x + width, y + height))
        self.text = Text(Point(x+width/2, y+height/2), name)
        self.rectangle.setFill("Pink")
        self.text.setTextColor("Purple")
        self.text.setSize(36)
        self.num = ''
    # Draws the die button     
    def draw(self, window):
        self.rectangle.draw(window.window)
        self.text.draw(window.window)
    # Draws the initial display of the die
    def rollDie(self):
        self.num = ran()
        self.text.setText(str(self.num))
        self.text.setTextColor('Black')
        return self.num



 
    
def main():    
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
    win = Board('Flying Chess', 750, 750, buttons, computerChesses)
    for button in buttons:
        button.draw(win)
    die.draw(win)
    for chess in computerChesses:
        chess.draw(win)

    for i in range(15):
        die.rollDie()
        next =  raw_input("Hit enter to continue")


    while not win.closed():
        win.update()


if __name__ == '__main__':
    main()
