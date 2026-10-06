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
        elif event.type == SDL_KEYDOWN and event.key in (SDLK_LEFT, SDLK_RIGHT, SDLK_UP, SDLK_DOWN):
            keys.add(event.key)
        elif event.type == SDL_KEYUP:
            keys.discard(event.key)


def update():
    global x, y, frame, facing

    if SDLK_LEFT in keys:
        x -= SPEED
    if SDLK_RIGHT in keys:
        x += SPEED
    if SDLK_UP in keys:
        y += SPEED
    if SDLK_DOWN in keys:
        y -= SPEED

    if SDLK_LEFT in keys:
        facing = IDLE_LEFT
    elif SDLK_RIGHT in keys:
        facing = IDLE_RIGHT

    x = clamp(x, FRAME_WIDTH // 2, WIDTH - FRAME_WIDTH // 2)
    y = clamp(y, FRAME_HEIGHT // 2, HEIGHT - FRAME_HEIGHT // 2)

    if keys:
        action = RUN_LEFT if facing == IDLE_LEFT else RUN_RIGHT
        frame = (frame + 1) % 8
    else:
        action = facing
        frame = 0
    return action


def draw(action):
    clear_canvas()
    background.draw(WIDTH // 2, HEIGHT // 2)
    boy.clip_draw(frame * FRAME_WIDTH, action * FRAME_HEIGHT,
                  FRAME_WIDTH, FRAME_HEIGHT, x, y)
    update_canvas()


while running:
    handle_events()
    draw(update())
    delay(DELAY)

close_canvas()
