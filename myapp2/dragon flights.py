import random
from pico2d import *

class Forest:
    def __init__(self):
        self.image = load_image('01.png')

    def draw(self):
        self.image.draw(192, 256)

class Dragon:
    LEFT_RUN, RIGHT_RUN, STAND, UP_RUN, DOWN_RUN = 0, 1, 2, 3, 4

    def __init__(self):
        self.x, self.y =192 , 60
        self.frame = 0
        self.state = self.STAND
        self.image = load_image('change1345.png')

    def handle_event(self, event):
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
        self.image.clip_draw(self.frame*157, 0, 157, 128, self.x, self.y)



def handle_events():
    global running
    global dragon
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
            running = False
        else:
            dragon.handle_event(event)
            pass


def main():

    open_canvas(384, 512)

    global dragon
    global running

    dragon = Dragon()
    forest = Forest()

    running = True;

    while running:
        handle_events()

        dragon.update()

        clear_canvas()
        forest.draw()

        dragon.draw()

        update_canvas()

        delay(0.08)

    close_canvas()


if __name__ == '__main__':
    main()
