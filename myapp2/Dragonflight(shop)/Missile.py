__author__ = 'Administrator'

from pico2d import *
from Ui import *

#cos(90 * (3.141592/180.0))
class Missile:
    def __init__(self, player, isMonster, Image):
        self.raby = player
        self.x, self.y = player.x, player.y

        self.xSize = 10
        self.ySize = 20
        if Image != None:
            self.image = Image

        elif isMonster == False:
            if player.Name == "Raby":
                if UI.WeaponLevel == 0:
                    self.image = load_image('bullet_raby.png')
            elif player.Name == "Sunny":
                self.image = load_image('bullet_sunny.png')
        else:
            self.image = load_image('bullet_mon.png')

        self.lifeTIme = 10.0
        self.isMonster = isMonster

    def update(self, frame_time):
        if self.isMonster == True:
            self.y -= 200 * frame_time
        else:
            self.y += 250 * frame_time
        self.lifeTIme -= frame_time

    def IsLive(self):
        return (self.lifeTIme <= 0.0)

    def draw(self):
        #if self.sunny.state in (self.sunny.RIGHT_RUN, self.sunny.LEFT_RUN, self.sunny.DOWN_RUN, self.sunny.UP_RUN, self.sunny.STAND):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - self.xSize, self.y - self.ySize, self.x + self.xSize, self.y + self.ySize


class Bomb:
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6

    def __init__(self, player):
        self.raby = player
        self.x, self.y = player.x, player.y
        self.xSize = 300
        self.ySize = 300

        self.frame = 0
        self.total_frames = 0

        self.image = load_image('bomb.png')

    def update(self, frame_time):
        self.total_frames += Bomb.FRAMES_PER_ACTION * Bomb.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 6
        self.y += 250 * frame_time

    def draw(self):
        self.image.clip_draw(self.frame * 550, 0, 550, 550, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - self.xSize, self.y - self.ySize, self.x + self.xSize, self.y + self.ySize