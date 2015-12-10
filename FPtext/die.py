# Huiji Ying & Yuhao Wan
# CS111, Carleton College
# Flying Chess, Final Project
# die.py

# A chunk of code to perform the function as a die in the game.
import random
from graphics import *
def ran():
    # Randomly generate a number in range 1 to 6.
    num = random.randint(1,6)
    # Present the number in a pop-out window.
    win = GraphWin('Die', 100, 100)
    die = Text(Point(50,50),num)
    die.setTextColor(color_rgb(0, 0, 0))
    die.setStyle('bold')
    die.setSize(30)
    die.draw(win)
    print num, 
    s = raw_input('>> die number')
    win.close()
    return num
