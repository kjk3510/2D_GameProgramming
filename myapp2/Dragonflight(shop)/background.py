__author__ = 'Administrator'

import random

from pico2d import *
import Ui

class DeathEffect:


    def __init__(self, target):
        self.image = load_image(target.death_Image)
        self.FRAMES_PER_ACTION = target.death_ifa

        self.x = target.x
        self.y = target.y
        self.total_frame = 0
        self.frame = 0
        self.image_num = target.death_num

        self.xSize = target.death_xSize
        self.ySize = target.death_ySize

        #self.effectTIme =
    def update(self, frame_time):
        self.total_frame += self.FRAMES_PER_ACTION * frame_time
        print(self.total_frame)
        self.frame = int(self.total_frame)

    def draw(self):
        self.image.clip_draw(self.xSize * self.frame, 0, self.xSize, self.ySize, self.x, self.y)

    def isEnd(self):
        return (self.image_num - 1 == self.frame)

class Background:

    PIXEL_PER_METER = (10.0 / 0.5) # 10 pixel 50 cm
    RUN_SPEED_KMPH = 30.0 # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 100

    global GameLevel

    def __init__(self, MapImage):
        self.image = MapImage
        self.image2 = MapImage
        self.total_frames = 0
        self.back_y1 = 0
        self.back_y2 = 800
        self.bgm = load_music('bgm_fir.mp3')
        self.bgm.set_volume(45)
        self.bgm.repeat_play()

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
        self.image.draw_to_origin(0, self.back_y2, 600, 800)

    def draw2(self):
        self.image.draw_to_origin(0, self.back_y1, 600, 800)