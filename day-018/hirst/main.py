from turtle import Screen, Turtle, TurtleScreen
from icecream import ic


def dashed_line_forward(turtle_obj: Turtle, distance: float, dash_size: float):
    cur_dist = 0
    while cur_dist < distance:
        turtle_obj.pendown()
        turtle_obj.forward(dash_size)
        cur_dist += dash_size

        turtle_obj.penup()
        turtle_obj.forward(dash_size)
        cur_dist += dash_size


def polygon(turtle_obj: Turtle, n: int, length: float):
    angle = 360 / n
    for _ in range(0, n):
        turtle_obj.forward(length)
        turtle_obj.right(angle)
        


if __name__ == "__main__":
    screen = Screen()
    screen.bgcolor('#800080')
    timmy = Turtle()
    timmy.shape('turtle')
    timmy.resizemode('auto')
    timmy.color('red')
    
    screen2 = Screen()
    screen2.screensize(int(1500), int(1500))
    screen2.bgcolor('orange')
    ic(screen)
    ic(screen2)
  
    
    # for _ in range(0, 4):
    #     timmy.left(-90)
    #     # timmy.forward(200)
    #     dashed_line_forward(timmy, 200, 10)
    
    polygon(timmy, 5, 150)
    
    ic(timmy.heading())
    
   
    screen.exitonclick()
    
