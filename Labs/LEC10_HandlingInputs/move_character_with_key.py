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

