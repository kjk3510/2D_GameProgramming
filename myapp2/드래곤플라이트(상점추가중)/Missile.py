__author__ = 'Administrator'

from pico2d import *

#cos(90 * (3.141592/180.0))
class Missile:
    def __init__(self, player, isMonster):
        self.raby = player
        self.x, self.y = player.x, player.y

        self.xSize = 10
        self.ySize = 20

        if isMonster == False:
            if player.Name == "Raby":
                self.image = load_image('bullet_raby.png')
            elif player.Name == "Sunny":
                self.image = load_image('bullet_sunny.png')
        else:
            self.image = load_image('bullet_mon.png')

        self.lifeTIme = 10.0
        self.isMonster = isMonster

    def update(self, frame_time):
        if self.isMonster == True:
            self.y -= 100 * frame_time
        else:
            self.y += 150 * frame_time
        self.lifeTIme -= frame_time

    def IsLive(self):
        return (self.lifeTIme <= 0.0)

    def draw(self):
        #if self.sunny.state in (self.sunny.RIGHT_RUN, self.sunny.LEFT_RUN, self.sunny.DOWN_RUN, self.sunny.UP_RUN, self.sunny.STAND):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - self.xSize, self.y - self.ySize, self.x + self.xSize, self.y + self.ySize
