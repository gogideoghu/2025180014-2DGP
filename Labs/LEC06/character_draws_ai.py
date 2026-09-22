from __future__ import annotations

import math
import sys

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum, auto
from pathlib import Path
from typing import Final, Iterable, Iterator, Sequence

import numpy as np
from pico2d import *


SCREEN_WIDTH: Final[int] = 800
SCREEN_HEIGHT: Final[int] = 600

FRAME_DELAY: Final[float] = 0.01

LEFT: Final[float] = 50.0
RIGHT: Final[float] = 750.0
BOTTOM: Final[float] = 50.0
TOP: Final[float] = 550.0


@dataclass(frozen=True, slots=True)
class Vector2:
    x: float
    y: float

    def __add__(self, other: Vector2) -> Vector2:
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector2) -> Vector2:
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> Vector2:
        return Vector2(self.x * scalar, self.y * scalar)

    @staticmethod
    def lerp(start: Vector2, end: Vector2, t: float) -> Vector2:
        return start + (end - start) * t


class PathType(Enum):
    CIRCLE = auto()
    RECTANGLE = auto()
    TRIANGLE = auto()


class CharacterRenderer:
    def __init__(self, image_path: Path) -> None:
        self.image = load_image(str(image_path))

    def draw(self, position: Vector2) -> None:
        clear_canvas()
        self.image.draw(position.x, position.y)
        update_canvas()
        delay(FRAME_DELAY)


class MovementPath(ABC):
    @abstractmethod
    def generate(self) -> Iterable[Vector2]:
        pass


class CirclePath(MovementPath):
    def __init__(
        self,
        center: Vector2,
        radius: float,
        segments: int = 360
    ) -> None:
        self.center = center
        self.radius = radius
        self.segments = segments

    def generate(self) -> Iterator[Vector2]:
        degrees = np.linspace(
            0.0,
            360.0,
            self.segments,
            endpoint=False
        )

        for degree in degrees:
            theta = math.radians(float(degree))

            yield Vector2(
                self.center.x + self.radius * math.cos(theta),
                self.center.y + self.radius * math.sin(theta)
            )


class PolylinePath(MovementPath):
    def __init__(
        self,
        vertices: Sequence[Vector2],
        steps_per_line: int = 100
    ) -> None:
        self.vertices = list(vertices)
        self.steps_per_line = steps_per_line

    def generate_line(
        self,
        start: Vector2,
        end: Vector2
    ) -> Iterator[Vector2]:

        parameter_values = np.linspace(
            0.0,
            1.0,
            self.steps_per_line + 1
        )

        for t in parameter_values:
            yield Vector2.lerp(
                start,
                end,
                float(t)
            )

    def generate(self) -> Iterator[Vector2]:
        vertex_count = len(self.vertices)

        for index in range(vertex_count):
            start = self.vertices[index]
            end = self.vertices[(index + 1) % vertex_count]

            yield from self.generate_line(start, end)


class MovementController:
    def __init__(
        self,
        renderer: CharacterRenderer
    ) -> None:
        self.renderer = renderer

    def execute(self, path: MovementPath) -> None:
        for position in path.generate():
            self.renderer.draw(position)


class PathFactory:
    @staticmethod
    def create(path_type: PathType) -> MovementPath:

        match path_type:

            case PathType.CIRCLE:
                return CirclePath(
                    center=Vector2(400.0, 300.0),
                    radius=200.0
                )

            case PathType.RECTANGLE:
                return PolylinePath(
                    vertices=[
                        Vector2(LEFT, TOP),
                        Vector2(RIGHT, TOP),
                        Vector2(RIGHT, BOTTOM),
                        Vector2(LEFT, BOTTOM)
                    ],
                    steps_per_line=140
                )

            case PathType.TRIANGLE:
                return PolylinePath(
                    vertices=[
                        Vector2(400.0, TOP),
                        Vector2(RIGHT, BOTTOM),
                        Vector2(LEFT, BOTTOM)
                    ],
                    steps_per_line=100
                )

            case _:
                raise ValueError(
                    f"지원하지 않는 경로입니다: {path_type}"
                )


def locate_character_asset() -> Path:
    current_file = Path(__file__).resolve()
    image_path = current_file.parent / "character.png"

    if not image_path.exists():
        raise FileNotFoundError(
            f"character.png 파일을 찾을 수 없습니다.\n"
            f"예상 경로: {image_path}"
        )

    return image_path


def initialize_application() -> MovementController:
    open_canvas(
        SCREEN_WIDTH,
        SCREEN_HEIGHT
    )

    character_path = locate_character_asset()

    renderer = CharacterRenderer(
        character_path
    )

    return MovementController(
        renderer
    )


def run_movement_sequence(
    controller: MovementController
) -> None:

    sequence: tuple[PathType, ...] = (
        PathType.CIRCLE,
        PathType.RECTANGLE,
        PathType.TRIANGLE
    )

    while True:
        for path_type in sequence:

            path = PathFactory.create(
                path_type
            )

            controller.execute(
                path
            )


def main() -> None:
    controller = initialize_application()

    try:
        run_movement_sequence(controller)

    except KeyboardInterrupt:
        print("사용자에 의해 프로그램이 종료되었습니다.")

    except Exception as error:
        print(
            f"[ERROR] 예상하지 못한 오류 발생: "
            f"{type(error).__name__}: {error}",
            file=sys.stderr
        )

    finally:
        close_canvas()


if __name__ == "__main__":
    main()