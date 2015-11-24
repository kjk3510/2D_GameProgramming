import random
import json
import os
import sys

import game_framework
import title_state
import select_state

from pico2d import *
from background import *
from sunny import *
from whdragon import *


first_time = 0
timesum = 0

name = "MainState"

sunny = None
background = None
whdragon = None
font = None

#Missile_1 = list()

def enter():
    global sunny, whdragon, background, team, missile_dr, first_time#, current_time
    sunny = Sunny()
    team = []
    for i in range(4):
        team.append(Whdragon(i))
    background = Background()

    first_time = get_time()

    #Missile_1 = list()

def exit( ):
    global sunny, team, background
    del(sunny)
    del(team)
    del(background)

def pause():
    pass

def resume():
    pass

def handle_events():
    global running
    global sunny
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
            game_framework.quit()
        else :
            sunny.handle_event(event)


def monsterRegen(frame_time):
    global timesum
    timesum += frame_time
    if timesum >= 5.0:
        timesum = 0.0
        for i in range(4):
            team.append(Whdragon(i))

def update():
    global first_time

    frame_time = get_time() - first_time

    monsterRegen(frame_time)

    #sunny.update(frame_time)

    #paladin.update(frame_time)

    sunny.update(frame_time)

    background.update(frame_time)

    missile = sunny.get_missile()

    for whdragon in team:
        whdragon.update(frame_time)

    for whdragon in team:
        if whdragon.collision(missile): # 내 총알이랑 몬스터랑 충돌일때
            #del(whitemonster)
            team.remove(whdragon)

        mon_missile = whdragon.get_missile()

        if sunny.collision(mon_missile) == True:
            print("충돌") #플레이어가 몬스터에게 총알 맞을떄 하면됨
            game_framework.change_state(select_state)
            break

    first_time = get_time()
    #for i in Missile_1:
    #    i.update()

def draw():
    #global Missile_1

    clear_canvas()
    background.draw()
    background.draw2()

    sunny.draw()

    for whdragon in team:
        whdragon.draw()

    #for i in Missile_1:
    #    i.draw()
    update_canvas()
   # delay(0.07)


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
