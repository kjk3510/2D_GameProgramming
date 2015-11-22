__author__ = 'Administrator'

import random

from pico2d import *

back_y1 = 0
back_y2 = 512

class Background:
    def __init__(self):
        self.image = load_image('01.png')
        self.image2 = load_image('01.png')

    def update(self, frame_time ):
        global back_y1, back_y2
        back_y1 -= 2
        back_y2 -= 2
        if(back_y2 == 0):
            back_y1 = 0
            back_y2 = 512

    def draw(self):
        global back_y1, back_y2
        self.image.draw_to_origin(0, back_y2, 384, 512)

    def draw2(self):
        global back_y1, back_y2
        self.image.draw_to_origin(0, back_y1, 384, 512)