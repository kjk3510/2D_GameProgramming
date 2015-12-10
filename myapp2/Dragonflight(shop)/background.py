__author__ = 'Administrator'

import random

from pico2d import *



class Background:

    PIXEL_PER_METER = (10.0 / 0.5) # 10 pixel 50 cm
    RUN_SPEED_KMPH = 30.0 # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 100

    def __init__(self):
        self.image = load_image('01.png')
        self.image2 = load_image('01.png')
        self.total_frames = 0
        self.back_y1 = 0
        self.back_y2 = 800

    def update(self, frame_time):
        #move_to_map = self.FRAMES_PER_ACTION * frame_time * self.ACTION_PER_TIME
        self.back_y1 -= self.FRAMES_PER_ACTION * frame_time
        self.back_y2 -= self.FRAMES_PER_ACTION * frame_time
        #back_y1 -= move_to_map
        #back_y2 -= move_to_map
        if(self.back_y1 <= -800):
            self.back_y1 = 0
            self.back_y2 = 800

    def draw(self):
        self.image.draw_to_origin(0, self.back_y2, 500, 800)

    def draw2(self):
        self.image.draw_to_origin(0, self.back_y1, 500, 800)