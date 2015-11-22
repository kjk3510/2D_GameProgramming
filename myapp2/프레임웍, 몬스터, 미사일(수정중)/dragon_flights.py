import random
import json
import os
import sys

import game_framework
import title_state

from pico2d import *
from background import *
from sunny import *
from whdragon import *


first_time = 0
timesum = 0

name = "MainState"

dragon = None
background = None
whitemonster = None
font = None

#Missile_1 = list()

def enter():
    global dragon, whitemonster, background, team, missile_dr, first_time#, current_time
    dragon = Sunny()
    team = []
    for i in range(5):
        team.append(Whitemonster(i))
    background = Background()

    first_time = get_time()

    #Missile_1 = list()


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

def monsterRegen(frame_time):
    global timesum
    timesum += frame_time
    if timesum >= 5.0:
        timesum = 0.0
        for i in range(5):
            team.append(Whitemonster(i))

def update():
    global first_time

    frame_time = get_time() - first_time

    monsterRegen(frame_time)

    dragon.update(frame_time)
    background.update(frame_time)

    missile = dragon.get_missile()

    for whitemonster in team:
        whitemonster.update(frame_time)

    for whitemonster in team:
        if whitemonster.collision(missile): # 내 총알이랑 몬스터랑 충돌일때
            #del(whitemonster)
            team.remove(whitemonster)

        mon_missile = whitemonster.get_missile()
        if dragon.collision(mon_missile) == True:
             print("충돌") #플레이어가 몬스터에게 총알 맞을떄 하면됨

    first_time = get_time()
    #for i in Missile_1:
    #    i.update()

def draw():
    #global Missile_1

    clear_canvas()
    background.draw()
    background.draw2()
    dragon.draw()
    for whitemonster in team:
        whitemonster.draw()
    #for i in Missile_1:
    #    i.draw()
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
