import game_framework
import select_state
from pico2d import *


name = "TitleState"
image = None


def enter():
    global image
    image = load_image('dragon title_1.png')


def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(select_state)


def draw():
    clear_canvas()
    image.draw_to_origin(0, 0, 600, 800)
    update_canvas()






def update():
    pass


def pause():
    pass


def resume():
    pass






