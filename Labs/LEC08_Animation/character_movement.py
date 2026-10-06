from pico2d import *


# Drill 9: arrow-key movement with sprite-sheet animation.

WIDTH = 800
HEIGHT = 600
FRAME_WIDTH = 100
FRAME_HEIGHT = 100
SPEED = 5
DELAY = 0.05

IDLE_RIGHT = 0
IDLE_LEFT = 1
RUN_RIGHT = 2
RUN_LEFT = 3

open_canvas(WIDTH, HEIGHT)
background = load_image('TUK_GROUND.png')
boy = load_image('animation_sheet.png')

running = True
x = WIDTH // 2
y = HEIGHT // 2
frame = 0
facing = IDLE_RIGHT
keys = set()


def clamp(value, low, high):
    return max(low, min(value, high))


def handle_events():
    global running

    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
