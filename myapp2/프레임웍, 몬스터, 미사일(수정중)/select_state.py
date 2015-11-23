__author__ = 'Administrator'


import game_framework
import main_raby
import main_sunny
from pico2d import *


name = "SelectState"
image = None


def enter():
    global image
    image = load_image('selected.png')


def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    global x, y
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, 512 - event.y

        elif event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x, 512 - event.y
            if x > 47 and x < 168 and y > 190 and y < 312:
                game_framework.change_state(main_sunny)
            if x > 215 and x < 335 and y > 190 and y < 312:
                game_framework.change_state(main_raby)

        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            #elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            #    game_framework.change_state(main_sunny)


def draw():
    clear_canvas()
    image.draw_to_origin(0, 0, 384, 512)
    update_canvas()






def update():
    pass


def pause():
    pass


def resume():
    pass

