from itertools import cycle
from bot import Bot
import random
import sys

import pygame
from pygame.locals import *

bot = Bot()

SCREENWIDTH  = 288
SCREENHEIGHT = 512
# amount by which base can maximum shift to left
PIPEGAPSIZE  = 100 # gap between upper and lower part of pipe
BASEY        = SCREENHEIGHT * 0.79
# image, sound and hitmask  dicts
IMAGES, HITMASKS = {}, {}

# list of all possible players (tuple of 3 positions of flap)
PLAYERS_LIST = (
    # red bird
    (
        'assets/sprites/redbird-upflap.png',
        'assets/sprites/redbird-midflap.png',
        'assets/sprites/redbird-downflap.png',
    ),
    # blue bird
    (
        # amount by which base can maximum shift to left
        'assets/sprites/bluebird-upflap.png',
        'assets/sprites/bluebird-midflap.png',
        'assets/sprites/bluebird-downflap.png',
    ),
    # yellow bird
    (
        'assets/sprites/yellowbird-upflap.png',
        'assets/sprites/yellowbird-midflap.png',
        'assets/sprites/yellowbird-downflap.png',
    ),
)
