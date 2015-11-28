__author__ = 'Administrator'

import random

from pico2d import *
from Missile import *
from game_framework import *

class CoinPos:
    def __init__(self, x, y):
        self.x = x
        self.xDir = random.randint(-15, 15)
        self.y = y
        self.xSize = 32/2
        self.ySize = 32/2
        self.lifeTime = 1.5

    def update(self, frame_time):
        if self.lifeTime > 0.0 :
            self.x += self.xDir * frame_time
            self.y += random.randint(15, 20) * frame_time
            self.lifeTime -= frame_time
        else :
            self.y -=( 80 * frame_time)
            self.lifeTime -= frame_time

    def get_bb(self):
        return self.x - self.xSize, self.y - self.ySize, self.x + self.xSize, self.y + self.ySize


class Coin:
    image = None
    FLYING = 0

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    def __init__(self):
        self.xSize = 32/2
        self.ySize = 32/2
        num = random.randint(1, 4)

        #self.x, self.y = 35 + 70 * num, 510
        self.frame = 0
        self.total_frames = 0
        self.CoinList = []
        # self.run_frames = 0
        # self.state_frames = 0
        # self.state = self.FLYING
        if Coin.image == None:
            Coin.image = load_image('coin.png')

    def __del__(self):
        for i in self.CoinList:
            self.CoinList.remove(i)

    def update(self, frame_time):
        self.total_frames += Whdragon.FRAMES_PER_ACTION * Whdragon.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 4
        #self.frame = (self.frame + 1) % 4

        for i in self.CoinList:
            i.update(frame_time)

    def collision(self, player):
        for i in self.CoinList:
            if collide(i, player) :
                self.CoinList.remove(i)
                return True
        return False

    def NewCoin(self, monster):
        self.CoinList.append(CoinPos(monster.x, monster.y))

    def NewCoinMany(self, monster, index):
        for i in range(index):
            self.CoinList.append(CoinPos(monster.x + random.randint(-5, 5), monster.y + random.randint(-5, 5) ))

    def draw(self):
        for i in self.CoinList:
            Coin.image.draw(i.x, i .y)



class Whdragon:
    image = None
    FLYING = 0

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4
    Missile = None
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
        print("등장!!!")
        self.xSize = 76/2
        self.ySize = 72/2
        #num = random.randint(1, 4)
        self.hp = 2
        self.x, self.y = 30 + 70  * num, 510
        self.frame = 0
        self.total_frames = 0
        #self.Missile = []
        self.attackDelay = random.randint(3, 5)
        # self.run_frames = 0
        # self.state_frames = 0
        # self.state = self.FLYING
        if Whdragon.Missile == None:
            Whdragon.Missile = list()
        if Whdragon.image == None:
            Whdragon.image = load_image('whdragon.png')

    def __del__(self):
        pass
        #for i in self.Missile:
            #del(i)
        #    self.Missile.remove(i)

    def update(self, frame_time):
        self.total_frames += Whdragon.FRAMES_PER_ACTION * Whdragon.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 4
        #self.frame = (self.frame + 1) % 4
        if self.y > 200:
            self.y -= 40 * frame_time

        self.attackDelay -= frame_time
        if self.attackDelay < 0.0 :
            print("Append!!")
            Whdragon.Missile.append(Missile(self, True))
            self.attackDelay = 4.0


    def MissileUpdate(frame_time):
        #for i in self.Missile:
        for i in Whdragon.Missile:
            i.update(frame_time)

            if i.IsLive() == True:
                Whdragon.Missile.remove(i)

    def collision(self, missile, damage = 1):
        for i in missile:
            if collide(self, i) :
                self.hp-=damage
                missile.remove(i)
                return True

        return False

    def IsDie(self):
        if self.hp <= 0:
            return True
        return False

    def draw(self):
        self.image.clip_draw(self.frame*76, 0, 76, 51, self.x, self.y)
        draw_rectangle(*self.get_bb())

       # for i in self.Missile:
        #    i.draw()

    def MissileDraw(null):
        for i in Whdragon.Missile:
            i.draw()

    #def get_missile(self):
    def get_missile(null):
        return Whdragon.Missile

    def ClearMissile(null):
        for i in Whdragon.Missile:
            Whdragon.Missile.remove(i)
            del(i)
        del(Whdragon.Missile)
        Whdragon.Missile = list()

    def get_bb(self):
        return self.x - self.xSize, self.y - self.ySize, self.x + self.xSize, self.y + self.ySize