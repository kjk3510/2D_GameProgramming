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
monster = None
font = None
missile_dr = None

Missile = list()

class Background:
    def __init__(self):
        self.image = load_image('01.png')

    def draw(self):
        self.image.draw(192, 256)


class Monster:
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
        if Monster.image == None:
            Monster.image = load_image('monster.png')

    def update(self):
        self.frame = (self.frame + 1) % 3
        self.y -= 5

    def draw(self):
        self.image.clip_draw(self.frame*154, 0, 157, 128, self.x, self.y)


class Dragon:
    LEFT_RUN, RIGHT_RUN, STAND, UP_RUN, DOWN_RUN = 0, 1, 2, 3, 4

    global missile_dr

    def __init__(self):
        self.x, self.y =192 , 60
        self.frame = 0
        self.state = self.STAND
        self.image = load_image('change1234.png')

    def handle_event(self, event):
        if self.state in (self.RIGHT_RUN, self.LEFT_RUN, self.DOWN_RUN, self.UP_RUN, self.STAND):
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                Missile.apend(missile(missile_dr.direction))

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
        self.frame = (self.frame + 1) % 3
        if self.state == self.RIGHT_RUN:
            self.x = min(324, self.x + 10)
        elif self.state == self.LEFT_RUN:
            self.x = max(60, self.x - 10)
        elif self.state == self.UP_RUN:
            self.y = min(512, self.y + 10)
        elif self.state == self.DOWN_RUN:
            self.y = max(0, self.y - 10)
        pass

    def draw(self):
        self.image.clip_draw(self.frame*154, 0, 157, 128, self.x, self.y)

class missile:
    global dragon
    def __init__(self):
        self.x2, self.y2 = self.x, self.y = dragon.x, dragon.y
        self.missile_frame = 0
        self.image = load_image('bullet_01.png')
        self.direction = dir
        if dir == 1 :
            self.image = load_image('bullet_01.png')
        elif dir == 0 :
            self.direction = -1

    def update(self):
        self.missile_frame = 0
        self.y += (5 * self.direction)

    def draw(self):
        if dragon.state in (dragon.RIGHT_RUN, dragon.LEFT_RUN, dragon.DOWN_RUN, dragon.UP_STAND, dragon.STAND):
            self.image.draw(self.x, self.y)


def enter():
    global dragon, monster, background, team, missile_dr
    dragon = Dragon()
    team = [Monster() for i in range(4)]
    background = Background()


def exit():
    global dragon, monster, background, missile_dr
    del(dragon)
    del(monster)
    del(background)
    del(missile_dr)

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
    for monster in team:
        monster.update()

    for i in Missile:
        if i.y < 512:
            i.update()
        if i.y > 512 :
            Missile.remove(i)
        if i.y < 40:
            Missile.remove(i)

def draw():
    clear_canvas()
    background.draw()
    dragon.draw()
    for monster in team:
        monster.draw()
    for i in Missile:
        if 40 < i.y < 512:
            i.draw
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
