import random
import json
import os
import sys

import game_framework
import title_state
import select_state
import Shop
import game_over

from pico2d import *
from background import *
#from raby import *
#from sunny import *
from Player import *
from whdragon import *
from Ui import *
from boss import *

first_time = 0
timesum = 0
timeboss = 0
#boss_time = 10.0
name = "MainState"

#raby = None
background = None
whdragon = None
font = None
player = None
coin = None
#Missile_1 = list()
ui = None
effect = list()

def enter():
    global player, character, whdragon, background, team, missile_dr, first_time, coin, PlayerName, effect, hit#, current_time
    #ui = UI(None)
    #ui = UI()
   # print("1", UI.name)
   # for i in Whdragon.Missile:
        #Whdragon.Missile.remove(i)
        #del(i)
    UI.boss_time = 30.0
    player = Player()
    team = []

    #if UI.GameLevel == 1 :
    #    for i in range(6):
    #        if random.randint(0, 2) != 0 :
    #            team.append(Whdragon(i, 'slime die.png'))
    if UI.GameLevel >= 0 :
        for i in range(7):
            if random.randint(0, 2) != 0 :
                team.append(Whdragon((i*1.1), None))

    background = Background(UI.GetMapImage(None))

    first_time = get_time()
    coin = Coin()
    effect = list()
    #Missile_1 = list()

def exit( ):
    global player, team, background, coin, effect
    for i in team:
        team.remove(i)
    del(team)
    del(player)

    del(background)
    del(coin)
    Whdragon.ClearMissile(None)

    for i in effect:
        effect.remove(i)
        del(i)

def pause():
    pass

def resume():
    pass

def handle_events():
    global running
    global player
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
            game_framework.quit()
        elif (event.type == SDL_KEYDOWN and event.key == SDLK_1 ):
            # 미사일 지우기
            Whdragon.ClearMissile(None)
        else :
            player.handle_event(event)


def monsterRegen(frame_time):
    global timesum
    timesum += frame_time

    if timesum >= 8.0:
        timesum = 0.0
        for i in range(7):
            if random.randint(0, 1) == 1 :
                team.append(Whdragon(i, None))


def bossRegen(frame_time):
    global timeboss
    timeboss += frame_time

    if timeboss >= 30.0:
        timesum = 0.0
        for i in range(1):
            if random.randint(0, 1) == 1 :
                team.append(whdragon(i, None))


def update():
    global first_time, coin

    frame_time = get_time() - first_time
    first_time = get_time()

    UI.Update(frame_time)
    for i in effect:
        i.update(frame_time)
        if i.isEnd() == True:
            effect.remove(i)
            del(i)


    monsterRegen(frame_time)

    #raby.update(frame_time)

    #paladin.update(frame_time)
    coin.update(frame_time)
    if coin.collision(player) == True:
        #ui=UI() 이렇게 클래스 만들지말고 반드시 UI.Addgold
        UI.AddGold(random.randint(1, 3))

    player.update(frame_time)

    background.update(frame_time)

    missile = player.get_missile()

    for whdragon in team:
        whdragon.update(frame_time)
        #collision(미사일, 데미지) collision(미사일)하면 1씩 깎임
        if whdragon.collision(missile, 2) == True: # 내 총알이랑 몬스터랑 충돌일때
            #coin.NewCoinMany(whdragon, 5)
            Player.hit(None)

            #hp가 0이면 True
            if whdragon.IsDie() == True:
                coin.NewCoin(whdragon)
                team.remove(whdragon)
                effect.append(DeathEffect(whdragon))
                del(whdragon)

    #이거는 미사일들 업데이트
    Whdragon.MissileUpdate(frame_time)

   # for whdragon in team:
    mon_missile = Whdragon.get_missile(None)

    if player.collision(mon_missile) == True:
        #  print("충돌") #플레이어가 몬스터에게 총알 맞을떄 하면됨
        game_framework.change_state(game_over)
        #break


    if UI.InitBoss(None) == True :
        print("보스등장!")
        NextStage()

    #for i in Missile_1:
    #    i.update()


def NextStage():
    UI.GameLevel+=1
    UI.boss_time = 30.0
    game_framework.change_state(Shop)


def draw():
    #global Missile_1

    clear_canvas()
    background.draw()
    background.draw2()

    player.draw()

    for i in effect:
        i.draw()

    for whdragon in team:
        whdragon.draw()
    #미사일들 그리기
    Whdragon.MissileDraw(None)
    coin.draw()
    UI.draw(None)

    #for i in Missile_1:
    #    i.draw()
    update_canvas()
    #delay(0.07)


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
