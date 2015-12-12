__author__ = 'Administrator'

from Ui import *

__author__ = 'Administrator'

import game_framework
import mainGame
from Ui import *
from pico2d import *

ui = None
name = "Shop"
image = None
buy_weapon = None
character = None

def enter():
    global image, ui, buy_weapon
    image = load_image('shop_1.png')
    UI.MakeImage(None)
    buy_weapon = None
    buy_weapon = UI.ChangeWeapon(buy_weapon)


def exit():
    global image, buy_weapon
    del(image)
    del(buy_weapon)


def handle_events():
    events = get_events()
    global x, y, PlayerName, ui, buy_weapon
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, 800 - event.y

        elif event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x, 800 - event.y

            if x > 40 and x < 190 and y > 350 and y < 530 :
                buy_weapon = ItemBuy('weapon', buy_weapon)
            if x > 225 and x < 375 and y > 590 and y < 765 :
                UI.AddArmor(None)

        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(mainGame)
            #elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            #    game_framework.change_state(main_sunny)


def draw():
    global buy_weapon
    clear_canvas()
    image.draw_to_origin(0, 0, 600, 800)
    if buy_weapon != None:
        buy_weapon.draw(300, 400)
        print(UI.name, UI.Type, UI.WeaponLevel)
    update_canvas()



def update():
    pass


def pause():
    pass


def resume():
    pass

