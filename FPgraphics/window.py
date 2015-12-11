# Huiji Ying & Yuhao Wan
# CS111, Carleton College
# Flying Chess, Final Project
# window.py

# a chunk of code to create the initial window of the game, which displays
# two buttons: help and play. Help leads to another window of rules
# play leads to the window containing the game board.

from images import *
from graphics import *

# draws the initial user interface of the game
def drawInitUI(win, x, y):
    text = Text(Point(x/2,y/3),'Flying Chess')
    text.setTextColor(color_rgb(0,0,0))
    text.setStyle('bold')
    text.setSize(36)
    text.draw(win)
# set the parameters of the two buttons on the window
    button('Play', x/12, y/2+10)
    button('Help', x*8/12, y/2+10)

# draws the button on the window    
def button(text, x, y):
    rect = Rectangle(Point(x,y),Point(x+150,y+50))
    rect.setFill('orange')
    string = Text(Point(x+75,y+25),text)
    string.setStyle('bold')
    string.setSize(20)
    rect.draw(win)
    string.draw(win)
    
def mouseCoordinate(point):
    return point.getX(), point.getY()

# enable mouse click on the two buttons
def click():
    click = win.getMouse()
    x,y = mouseCoordinate(click)
    if x in range(47,198) and y in range(210,261):
        play()
    elif x in range(373,524) and y in range(210,261):
        helpText()
        return 1
    else:
        return 1 

# draws the window on Help (rules of the game)
def helpText():
    win = GraphWin('Help', 400, 400)
    rule = Text(Point(50,20), "Rules:")
    rule.setStyle("bold italic")
    rule.setSize(20)
    rule.draw(win)
    rules = open("help.txt")
    n = 0
    for l in rules:
        r = Text(Point(200,15*n+75), l)
        r.draw(win)
        n += 1

# close the initial window while game starts   
def play():
    win.close()
    import system
    

if __name__ == '__main__':
    win = GraphWin('Flying Chess', 560, 400)
    backgroundImage = Image(Point(282,180), "plane.gif")
    backgroundImage.draw(win)
    print "Please click on Play to start the game!"
    print "Or click on Help to see the rules."
    drawInitUI(win, 560, 400)
    clickTester = 1
    while clickTester:
        clickTester = click()
    
    
    