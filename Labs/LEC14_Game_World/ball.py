"""A projectile that removes itself after leaving the canvas."""

from pathlib import Path

from pico2d import get_canvas_width, load_image

import game_world


ASSET_DIR = Path(__file__).resolve().parent


class Ball:
    WIDTH = 21

    def __init__(self, x, y, velocity):
        self.x = float(x)
        self.y = float(y)
        self.velocity = velocity
        self.image = load_image(str(ASSET_DIR / 'ball21x21.png'))

    def update(self):
        self.x += self.velocity
        half_width = self.WIDTH / 2
        if self.x < -half_width or self.x > get_canvas_width() + half_width:
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)
