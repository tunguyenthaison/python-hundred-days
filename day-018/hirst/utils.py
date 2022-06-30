import secrets
from threading import currentThread
import turtle
import random
from colour import Color
from icecream import ic


def random_color() -> str:
    """ Get a random color in rgb

    Returns:
        str: the rgb representation of the randomly generated color
    """
    rand_int = random.randint(0, 255)
    color = Color(pick_for=rand_int)
    return color.get_rgb()


def random_walk(duration: int, step_size: int = 5) -> None:
    """Draw a random walk with the turtle module

    Args:
        duration (int): number of steps
        step_size (int, optional): pixel size of each step. Defaults to 5.
    """
    walker = turtle.Turtle()
    screen = walker.getscreen()
    current_step = 0
    # print(screen.screensize())
    # walker.goto(400, 300)
    # walker.goto(0, 405)
    # ic(screen.window_height())
    # ic(screen.window_width())
    walker.speed('fastest')
    walker.pensize(5)
    while current_step < duration:
        walker.pencolor(random_color())
        random_heading = random.choice(seq=[0, 90, 180, 270])
        walker.setheading(random_heading)
        walker.forward(step_size)
        current_step += 1
    screen.exitonclick()


if __name__ == "__main__":
    random_walk(duration=200000, step_size=20)
