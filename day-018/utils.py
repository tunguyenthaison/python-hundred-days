# from turtle import Turtle
import turtle
import random
from colour import Color
from icecream import ic


def polygon(turtle_obj: turtle.Turtle, n: int, length: float = 200):
    angle = 360 / n
    for _ in range(0, n):
        turtle_obj.forward(length)
        turtle_obj.right(angle)


def random_color() -> str:
    """ Get a random color in rgb

    Returns:
        str: the rgb representation of the randomly generated color
    """
    rand_int = random.randint(0, 255)
    color = Color(pick_for=rand_int)
    return color.get_rgb()


def is_in_box(x: int, y: int, width: int, height: int) -> bool:
    """Check if a point (x,y) is in the box

    Args:
        x (int): x-coordinate
        y (int): y-coordinate
        width (int): width of the box
        height (int): height of the box

    Returns:
        bool: True/False if the point is in or not
    """
    X_max = width // 2
    Y_max = height // 2
    return (x >= -X_max and x <= X_max and y >= -Y_max and y <= Y_max)


def dashed_line_forward(turtle_obj: turtle.Turtle, distance: float, dash_size: float) -> None:
    cur_dist = 0
    while cur_dist < distance:
        turtle_obj.pendown()
        turtle_obj.forward(dash_size)
        cur_dist += dash_size

        turtle_obj.penup()
        turtle_obj.forward(dash_size)
        cur_dist += dash_size


def random_walk(duration: int, step_size: int = 5, pensize: int = 5, reflex=False) -> None:
    """Draw a random walk with the turtle module

    Args:
        duration (int): number of steps
        step_size (int, optional): pixel size of each step. Defaults to 5.
    """
    walker = turtle.Turtle()
    screen = walker.getscreen()
    walker.speed('fastest')
    walker.pensize(pensize)

    current_step = 0

    width = screen.window_width()
    X_max = width // 2
    height = screen.window_height()
    Y_max = height // 2

    # plot the bounding box
    # walker.pencolor('red')
    # walker.penup()
    # walker.setposition(-X_max, Y_max)
    # walker.pendown()
    # walker.setheading(0)
    # for _ in range(0, 2):
    #     walker.forward(width)
    #     walker.right(90)
    #     walker.forward(height)
    #     walker.right(90)

    # the random walk
    walker.setposition(0, 0)
    while current_step < duration:
        walker.pencolor(random_color())
        if reflex:
            next_step_ok = False
            while not next_step_ok:
                random_heading = random.choice(seq=[0, 90, 180, 270])
                walker.setheading(random_heading)
                walker.forward(step_size)
                new_position = walker.position()
                x, y = new_position
                next_step_ok = is_in_box(x, y, width, height)
                if not is_in_box(x, y, width, height):
                    walker.backward(step_size)
        else:
            random_heading = random.choice(seq=[0, 90, 180, 270])
            walker.setheading(random_heading)
            walker.forward(step_size)
        current_step += 1
    screen.exitonclick()


def spinograph(radius: float = 100, number_steps: int = 20, pensize: int = 5):
    walker = turtle.Turtle()
    screen = walker.getscreen()
    walker.speed('fastest')
    walker.pensize(pensize)

    angle = 360 / number_steps
    current_step = 0

    # reset the position heading
    # walker.hideturtle()
    # walker.setheading(180)
    # walker.showturtle()

    # plot
    while current_step < number_steps:
        walker.color()
        walker.pencolor(random_color())
        walker.circle(radius)
        # change the heading
        walker.setheading(walker.heading() + angle)
        current_step += 1
    screen.exitonclick()


if __name__ == "__main__":
    # random_walk(duration=200000, step_size=20)
    spinograph(number_steps=200, pensize=1)
