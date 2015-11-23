__author__ = 'Administrator'

import random

from pico2d import *

back_y1 = 0
back_y2 = 512

class Background:

    PIXEL_PER_METER = (10.0 / 0.5) # 10 pixel 50 cm
    RUN_SPEED_KMPH = 20.0 # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.image = load_image('01.png')
        self.image2 = load_image('01.png')
        self.total_frames = 0

    def update(self, frame_time):
        global back_y1, back_y2
        back_y1 -= 4
        back_y2 -= 4
        if(back_y2 == 0):
            back_y1 = 0
            back_y2 = 512

    def draw(self):
        global back_y1, back_y2
        self.image.draw_to_origin(0, back_y2, 384, 512)

    def draw2(self):
        global back_y1, back_y2
        self.image.draw_to_origin(0, back_y1, 384, 512)