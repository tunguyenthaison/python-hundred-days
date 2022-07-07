# run from /root of the repo
from turtle import Screen, Turtle, TurtleScreen
import turtle
from icecream import ic
import colorgram
import numpy as np
import random
import utils
import os
import io
from PIL import Image
import PIL


def hirst_painting(size: int = 2, step_distance: int = 50):

    padding = 50
    # Extract 30 colors from an image.
    colors = colorgram.extract('day-018/hirst.jpg', 40)
    colors_rgb = [np.array([color.rgb.r, color.rgb.g, color.rgb.b]) / 255
                  for color in colors]

    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.setup(width=500, height=500)
    screen.title("Hirst's style painting")

    walker = turtle.Turtle()
    walker.speed('fastest')
    walker.pensize(2)

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

    # frame count to save for animation
    # os.mkdir('./day-018/outs')
    frame_index = 1

    # initialize y-position
    y = 0
    while y < y_steps:
        # reset current x-position
        x = 0
        while x < x_steps:
            walker.dot(size, random.choice(colors_rgb))
            walker.forward(step_distance)
            x += 1

            # save the frame
            cv = turtle.getcanvas()
            ps_name = os.path.join("./day-018/ps_outs", f'out_{frame_index}.ps')
            cv.postscript(file=ps_name,
                          colormode='color')
            psimage = Image.open(ps_name)
            png_name = os.path.join("./day-018/png_outs",
                                    f'out_{frame_index}.png')
            psimage.save(png_name)
            frame_index += 1

        y += 1
        walker.setposition([root_position[0],
                            root_position[1] + y * step_distance])

    # screen.exitonclick()


if __name__ == "__main__":
    hirst_painting(size=20, step_distance=50)
    # make a gif file
    import glob

    # Create the frames
    frames = []
    imgs = glob.glob("./day-018/png_outs/*.png")
    for img in imgs:
        new_frame = Image.open((img))
        frames.append(new_frame)

    # Save into a GIF file that loops forever
    frames[0].save('./day-018/output.gif',
                   format='gif',
                   append_images=frames[1:],
                   save_all=True,
                   duration=10,
                   loop=0)
