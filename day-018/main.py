# run from /root of the repo
from turtle import Screen, Turtle, TurtleScreen, width
import turtle
from icecream import ic
import colorgram
import numpy as np
import random
import utils


def hirst_painting(size: int = 2, step_distance: int = 50):

    padding = 50
    # Extract 30 colors from an image.
    colors = colorgram.extract('day-018/hirst.jpg', 40)
    colors_rgb = [np.array([color.rgb.r, color.rgb.g, color.rgb.b]) / 255
                  for color in colors]

    walker = turtle.Turtle()
    walker.speed('fastest')
    walker.pensize(2)
    screen = turtle.Screen()
    screen.title("Hirst's style painting")

    width, height = screen.window_width(), screen.window_height()
    X_max, Y_max = width // 2, height // 2

    walker.penup()
    walker.hideturtle()
    # account for left and bottom padding
    root_position = [-X_max + padding, -Y_max + padding]
    walker.setposition(root_position)

    # walker.pendown()
    # walker.showturtle()

    x_steps = 2 * X_max // step_distance - 1  # account for right-padding
    y_steps = 2 * Y_max // step_distance - 1  # account for top-padding

    # initialize y-position
    y = 0
    while y < y_steps:
        # reset current x-position
        x = 0
        while x < x_steps:
            walker.dot(size, random.choice(colors_rgb))
            walker.forward(step_distance)
            x += 1
        y += 1
        walker.setposition([root_position[0],
                            root_position[1] + y * step_distance])

    screen.exitonclick()


if __name__ == "__main__":
    hirst_painting(size=20, step_distance=50)
