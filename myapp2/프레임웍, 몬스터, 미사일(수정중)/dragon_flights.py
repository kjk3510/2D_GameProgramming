import random
import json
import os
import sys

import game_framework
import title_state

from pico2d import *

name = "MainState"

dragon = None
background = None
whitemonster = None
font = None

Missile_1 = list()

back_y1 = 0
back_y2 = 512

class Background:
    def __init__(self):
        self.image = load_image('01.png')
        self.image2 = load_image('01.png')

    def update(self):
        global back_y1, back_y2
        back_y1 -= 2
        back_y2 -= 2
        if(back_y2 == 0):
            back_y1 = 0
            back_y2 = 512

    def draw(self):
        global back_y1, back_y2
        self.image.draw_to_origin(0, back_y2, 384, 512)

    def draw2(self):
        global back_y1, back_y2
        self.image.draw_to_origin(0, back_y1, 384, 512)


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

    def __init__(self):
        self.x, self.y = random.randint(40, 344), 480
        self.frame = 0
        # self.run_frames = 0
        # self.state_frames = 0
        # self.state = self.FLYING
        if Whitemonster.image == None:
            Whitemonster.image = load_image('whdragon.png')

    def update(self):
        self.frame = (self.frame + 1) % 4
        self.y -= 1

    def draw(self):
        self.image.clip_draw(self.frame*76, 0, 76, 51, self.x, self.y)


class Dragon:
    LEFT_RUN, RIGHT_RUN, STAND, UP_RUN, DOWN_RUN = 0, 1, 2, 3, 4

    def __init__(self):
        self.x, self.y =192 , 60
        self.frame = 0
        self.state = self.STAND
        self.image = load_image('sunny.png')

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if self.state in (self.RIGHT_RUN, self.LEFT_RUN, self.DOWN_RUN, self.UP_RUN, self.STAND):
                dragon.shooting()

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



    def update(self):
        self.frame = (self.frame + 1) % 4
        if self.state == self.RIGHT_RUN:
            self.x = min(374, self.x + 10)
        elif self.state == self.LEFT_RUN:
            self.x = max(10, self.x - 10)
        elif self.state == self.UP_RUN:
            self.y = min(452, self.y + 10)
        elif self.state == self.DOWN_RUN:
            self.y = max(60, self.y - 10)
        pass

    def draw(self):
        self.image.clip_draw(self.frame*128, 0, 128, 106, self.x, self.y)

    def shooting(self):
        newmissile = Missile(self.x, self.y)
        Missile_1.append(newmissile)

class Missile:
    global dragon
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.image = load_image('bullet_01.png')

    def update(self):
        self.y += 5
        # if(self.y > 512):
        #     self.y = 0
        #     del Missile_1

    def draw(self):
        if dragon.state in (dragon.RIGHT_RUN, dragon.LEFT_RUN, dragon.DOWN_RUN, dragon.UP_RUN, dragon.STAND):
            self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x-50, self.y-50, self.x+50, self.y+50

def enter():
    global dragon, whitemonster, background, team, missile_dr
    dragon = Dragon()
    team = [Whitemonster() for i in range(5)]
    background = Background()
    Missile_1 = list()


def exit( ):
    global dragon, monster, background
    del(dragon)
    del(whitemonster)
    del(background)

def pause():
    pass

def resume():
    pass

def handle_events():
    global running
    global dragon
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
            game_framework.quit()
        else:
            dragon.handle_event(event)
            pass

def update():
    dragon.update()
    background.update()
    global missile
    for whitemonster in team:
        whitemonster.update()

    for i in Missile_1:
        i.update()

def draw():
    clear_canvas()
    background.draw()
    background.draw2()
    dragon.draw()
    for whitemonster in team:
        whitemonster.draw()
    for i in Missile_1:
        i.draw()
    update_canvas()
    delay(0.07)


# def main():
#
#     open_canvas(384, 512)
#
#     global dragon
#     global running
#
#     dragon = Dragon()
#     background = Background()
#
#     running = True;
#
#     while running:
#         handle_events()
#
#         dragon.update()
#
#         clear_canvas()
#         background.draw()
#
#         dragon.draw()
#
#         update_canvas()
#
#         delay(0.07)
#
#     close_canvas()


if __name__ == '__main__':
    main()
