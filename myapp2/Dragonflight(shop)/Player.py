__author__ = 'Administrator'

import random

from game_framework import *
from pico2d import *
from Missile import *
from Ui import *

class Player:
    Name = None
    shoot_sound = None
    Die_sound = None
    hit_sound = None
    bomb_e_sound = None

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6

    LEFT_RUN, RIGHT_RUN, STAND, UP_RUN, DOWN_RUN = 0, 1, 2, 3, 4

    def __init__(self):
        self.x, self.y = 192, 60
        self.frame = 0
        self.total_frames = 0
        self.state = self.STAND
        Player.Name = UI.name
        if Player.Name == "Sunny":
            print("Sunny")
            self.image = load_image('sunny.png')
        elif Player.Name == "Raby":
            print("Raby")
            self.image = load_image('raby.png')
        self.xSize = 116/2
        self.ySize = 100/2

        if Player.shoot_sound == None:
            Player.shoot_sound = load_wav('ch_attack.wav')
            Player.shoot_sound.set_volume(32)
        if Player.hit_sound == None:
            Player.hit_sound = load_wav('critical.wav')
            Player.hit_sound.set_volume(40)
        if Player.bomb_e_sound == None:
            Player.bomb_e_sound = load_wav('explosion.wav')
            Player.bomb_e_sound.set_volume(40)

        self.Missile_1 = list()
        self.Bomb = list()

    def shoot(self):
        self.shoot_sound.play()

    def hit(self):
        Player.hit_sound.play()

    def bomb_e(self):
        self.bomb_e_sound.play()

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if self.state in (self.RIGHT_RUN, self.LEFT_RUN, self.DOWN_RUN, self.UP_RUN, self.STAND):
                self.shooting()
                Player.shoot(self)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_x):
            if self.state in (self.RIGHT_RUN, self.LEFT_RUN, self.DOWN_RUN, self.UP_RUN, self.STAND):
                self.bomb()
                Player.bomb_e(self)

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
        self.total_frames += Player.FRAMES_PER_ACTION * Player.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 4

        for i in self.Missile_1:
            i.update(frame_time)
            if i.IsLive() :
                self.Missile_1.remove(i)
        for i in self.Bomb:
            i.update(frame_time)

        if self.state == self.RIGHT_RUN:
            self.x = min(590, self.x + 200 * frame_time)
        elif self.state == self.LEFT_RUN:
            self.x = max(10, self.x - 200 * frame_time)
        elif self.state == self.UP_RUN:
            self.y = min(740, self.y + 200 * frame_time)
        elif self.state == self.DOWN_RUN:
            self.y = max(60, self.y - 200 * frame_time)
        pass

    def draw(self):
        self.image.clip_draw(self.frame*128, 0, 128, 106, self.x, self.y)
        draw_rectangle(*self.get_bb())
        for i in self.Missile_1:
            i.draw()
        if UI.ArmorGauge > 0 :
            UI.ArmorImage.draw(self.x, self.y)
        for i in self.Bomb:
            i.draw()

    def collision(self, missile):
        for i in missile:
            if collide(self, i) :
                missile.remove(i)
                del(i)
                if UI.ArmorGauge > 0 :
                    print("충격 흡수")
                    UI.ArmorGauge-=1
                    Player.hit(self)
                else:
                    return True

        return False

    def get_bb(self):
        return self.x - self.xSize, self.y - self.ySize, self.x + self.xSize, self.y + self.ySize

    def get_missile(self):
        return self.Missile_1

    def get_bomb(self):
        return self.Bomb

    def shooting(self):
        newmissile = Missile(self, False, UI.GetWeaponInGame(None))
        self.Missile_1.append(newmissile)

    def bomb(self):
        newbomb = Bomb(self)
        self.Bomb.append(newbomb)
        print("폭탄발사!")