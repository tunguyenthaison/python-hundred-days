from turtle import Screen, Turtle, TurtleScreen
from icecream import ic






        


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
    
