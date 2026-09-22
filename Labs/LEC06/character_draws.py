from os.path import abspath, dirname, join

from pico2d import *

open_canvas(800, 600)
image_path = join(dirname(abspath(__file__)), 'character.png')
boy = load_image(image_path)

#어떤 이유에서인지 character.png파일이 제대로 불러와지지 않아 해당 부분은 ai를 통해 수정하였습니다.

clear_canvas()
boy.draw(400, 300)
update_canvas()
delay(1)
close_canvas()

def move_circle():
    pass

def move_rectangle():
    pass

def move_triangle():
    pass

while True:
    move_circle()
    move_rectangle()
    move_triangle()
