__author__ = 'Administrator'

from pico2d import *

PlayerName = None

class UI:
    name = None
    gold = 0
    boss_time = 10.0

    item = None

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    LEFT_RUN, RIGHT_RUN, STAND, UP_RUN, DOWN_RUN = 0, 1, 2, 3, 4

    def __init__(self, name):
        if name != None:
            UI.name = name
        self.x, self.y = 192, 60
        self.frame = 0
        self.total_frames = 0
        self.state = self.STAND
        self.xSize = 128/2
        self.ySize = 106/2

    def AddGold(money):
        UI.gold += money
        print(UI.gold)

#self 쓰지말것*****************************************************************************
    def BuyItem(items):
        UI.item = items

    def Update(frame_time):
        if UI.boss_time > 0 :
            UI.boss_time -= frame_time
    def InitBoss(null):
        if UI.boss_time < 0 and UI.boss_time != -100:
            UI.boss_time = -100
            return True
        return False

    def handle_event(self, event):
        pass
