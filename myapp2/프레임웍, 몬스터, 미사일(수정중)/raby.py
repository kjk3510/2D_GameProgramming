__author__ = 'Administrator'

import random

from game_framework import *
from pico2d import *
from missile_raby import *

class Raby:
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    LEFT_RUN, RIGHT_RUN, STAND, UP_RUN, DOWN_RUN = 0, 1, 2, 3, 4

    def __init__(self):
        self.x, self.y = 192, 60
        self.frame = 0
        self.total_frames = 0
        self.state = self.STAND
        self.image = load_image('raby.png')

        self.xSize = 128/2
        self.ySize = 106/2

        self.Missile_1 = list()

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if self.state in (self.RIGHT_RUN, self.LEFT_RUN, self.DOWN_RUN, self.UP_RUN, self.STAND):
                self.shooting()

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state in (self.STAND, self.RIGHT_RUN, self.UP_RUN, self.DOWN_RUN):
                self.state = self.LEFT_RUN
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.state in (self.STAND, self.LEFT_RUN, self.UP_RUN, self.DOWN_RUN):
                self.state = self.RIGHT_RUN
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            if self.state in (self.STAND, self.RIGHT_RUN, self.LEFT_RUN, self.DOWN_RUN):
                self.state = self.UP_RUN
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            if self.state in (self.STAND, self.RIGHT_RUN, self.LEFT_RUN, self.UP_RUN):
                self.state = self.DOWN_RUN
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.state in (self.LEFT_RUN,):
                self.state = self.STAND
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.state in (self.RIGHT_RUN,):
                self.state = self.STAND
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_UP):
            if self.state in (self.UP_RUN,):
                self.state = self.STAND
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
            if self.state in (self.DOWN_RUN,):
                self.state = self.STAND

    def update(self, frame_time):
        self.total_frames += Raby.FRAMES_PER_ACTION * Raby.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 4

        for i in self.Missile_1:
            i.update(frame_time)
            if i.IsLive() :
                self.Missile_1.remove(i)

        if self.state == self.RIGHT_RUN:
            self.x = min(374, self.x + 70 * frame_time)
        elif self.state == self.LEFT_RUN:
            self.x = max(10, self.x - 70 * frame_time)
        elif self.state == self.UP_RUN:
            self.y = min(452, self.y + 70 * frame_time)
        elif self.state == self.DOWN_RUN:
            self.y = max(60, self.y - 70 * frame_time)
        pass

    def draw(self):
        self.image.clip_draw(self.frame*128, 0, 128, 106, self.x, self.y)

        for i in self.Missile_1:
            i.draw()

    def collision(self, missile):
        for i in missile:
            if collide(self, i) :
                return True

        return False

    def get_bb(self):
        return self.x - self.xSize, self.y - self.ySize, self.x + self.xSize, self.y + self.ySize

    def get_missile(self):
        return self.Missile_1

    def shooting(self):
        newmissile = Missile(self, False)
        self.Missile_1.append(newmissile)