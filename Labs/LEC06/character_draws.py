from os.path import abspath, dirname, join
import math
from pico2d import *

open_canvas(800, 600)
#어떤 이유에서인지 character.png파일이 제대로 불러와지지 않아 해당 부분은 ai를 통해 수정하였습니다.
image_path = join(dirname(abspath(__file__)), 'character.png')
boy = load_image(image_path)

clear_canvas()
boy.draw(400, 300)
update_canvas()
delay(1)
close_canvas()

def draw_boy(x, y):
    clear_canvas()
    boy.draw(x, y)
    update_canvas()
    delay(0.01)

degree = 0
theta = math.radians(degree)
x = 400 + 200 * math.cos(theta)
y = 300 + 200 * math.sin(theta)


def move_circle():
    for degree in range(360):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)

        clear_canvas()
        boy.draw(x, y)
        update_canvas()
        delay(0.01)

def move_top():
    print('top')
    pass
def move_right():
    print('right')
    pass
def move_bottom():
    print('bottom')
    pass    
def move_left():
    print('left')
    pass


def move_rectangle():
    move_top()
    move_right()
    move_bottom()
    move_left()

def move_triangle():
    print('triangle')

while True:
    move_circle()
    move_rectangle()
    move_triangle()
