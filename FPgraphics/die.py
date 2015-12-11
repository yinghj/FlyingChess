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
    return num