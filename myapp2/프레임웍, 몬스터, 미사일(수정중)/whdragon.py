__author__ = 'Administrator'

import random

from pico2d import *
from missile import *
from game_framework import *

class Whitemonster:
    image = None
    FLYING = 0

    # def handle_left_run(self):
    #     self.x -= 5
    #     self.run_frames += 1
    #     if self.x < 40:
    #         self.state = self.FLYING
    #         self.x = 40
    #     if self.run_frames == 150:
    #         self.state = self.FLYING
    #         self.state_frames = 0
    #
    # def handle_left_stand(self):
    #     self.state_frames += 1
    #     if self.state_frames == 100:
    #         self.state = self.FLYING
    #         self.run_frames = 0
    #
    #
    # def handle_right_run(self):
    #     self.x += 5
    #     self.run_frames += 1
    #     if self.x > 344:
    #         self.state = self.FLYING
    #     if self.run_frames == 150:
    #         self.state = self.FLYING
    #         self.state_frames = 0
    #
    #
    # def handle_right_stand(self):
    #     self.state_frames += 1
    #     if self.state_frames == 100:
    #         self.state = self.FLYING
    #         self.run_frames = 0

    def __init__(self, num):
        self.xSize = 76/2
        self.ySize = 72/2

        self.x, self.y = 35 + 70 * num, random.randint(400, 500)
        self.frame = 0
        self.Missile = []
        self.attackDelay = random.randint(3, 5)
        # self.run_frames = 0
        # self.state_frames = 0
        # self.state = self.FLYING
        if Whitemonster.image == None:
            Whitemonster.image = load_image('whdragon.png')
    def __del__(self):
        for i in self.Missile:
            #del(i)
            self.Missile.remove(i)

    def update(self, frame_time):
        self.frame = (self.frame + 1) % 4
        self.y -= 1

        self.attackDelay -= frame_time
        if self.attackDelay < 0.0 :
            self.Missile.append(Missile(self, True))
            self.attackDelay = 5.0

        for i in self.Missile:
            i.update(frame_time)

            if i.IsLive() == True:
                self.Missile.remove(i)

    def collision(self, missile):
        for i in missile:
            if collide(self, i) :
                return True

        return False

    def draw(self):
        self.image.clip_draw(self.frame*76, 0, 76, 51, self.x, self.y)

        for i in self.Missile:
            i.draw()

    def get_missile(self):
        return self.Missile

    def get_bb(self):
        return self.x - self.xSize, self.y - self.ySize, self.x + self.xSize, self.y + self.ySize