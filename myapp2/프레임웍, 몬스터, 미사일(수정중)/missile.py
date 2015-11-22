__author__ = 'Administrator'

from pico2d import *

#cos(90 * (3.141592/180.0))
class Missile:
    def __init__(self, Sunny, isMonster):
        self.sunny = Sunny
        self.x, self.y = Sunny.x, Sunny.y

        self.xSize = 10
        self.ySize = 20

        if isMonster == False:
            self.image = load_image('bullet_01.png')
        else:
            self.image = load_image('bullet_02.png')

        self.lifeTIme = 3.0
        self.isMonster = isMonster

    def update(self, frame_time):
        if self.isMonster == True:
            self.y -= 5
        else:
            self.y += 5
        self.lifeTIme -= frame_time

    def IsLive(self):
        return (self.lifeTIme <= 0.0)

    def draw(self):
        #if self.sunny.state in (self.sunny.RIGHT_RUN, self.sunny.LEFT_RUN, self.sunny.DOWN_RUN, self.sunny.UP_RUN, self.sunny.STAND):
        self.image.draw(self.x, self.y)


    def get_bb(self):
        return self.x - self.xSize, self.y - self.ySize, self.x + self.xSize, self.y + self.ySize