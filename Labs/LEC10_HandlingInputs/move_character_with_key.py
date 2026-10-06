from pico2d import *


# Drill 9: 키 입력으로 소년을 움직이고 sprite sheet를 애니메이션한다.

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
FRAME_WIDTH = 100
FRAME_HEIGHT = 100
MOVE_SPEED = 5
ANIMATION_DELAY = 0.05

IDLE_RIGHT = 0
IDLE_LEFT = 1
RUN_RIGHT = 2
RUN_LEFT = 3

open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
background = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x = CANVAS_WIDTH // 2
y = CANVAS_HEIGHT // 2
frame = 0
direction = IDLE_RIGHT
moving = False
pressed_keys = set()


def keep_on_screen(value, low, high):
    return max(low, min(value, high))


def handle_events():
    global running, moving

    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN:
            pressed_keys.add(event.key)
            moving = True
        elif event.type == SDL_KEYUP:
            pressed_keys.discard(event.key)
            moving = bool(pressed_keys)


def update():
    global x, y, direction, moving, frame

    if SDLK_LEFT in pressed_keys:
        x -= MOVE_SPEED
    if SDLK_RIGHT in pressed_keys:
        x += MOVE_SPEED

