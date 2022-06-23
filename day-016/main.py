""" Script for testing out the turtle module
"""
from time import sleep
from turtle import Turtle, Screen
import turtle
from icecream import ic

timmy = turtle.Turtle()
timmy.dot(size=20)
timmy.circle(200, 180)
timmy.color("blue")
g = timmy.stamp()
timmy.backward(100)
timmy.clearstamp(g)
sleep(1)


screen = timmy.getscreen()
screen.bgcolor("orange")

s = turtle.Shape("compound")
print(s)
poly1 = ((0, 0), (10, -5),(0,10),(-10,-5))
s.addcomponent(poly1, "red", "blue")
poly2 = ((0,0),(10,-5),(-10,-5))
s.addcomponent(poly2, "blue", "red")
print(s)
turtle.register_shape("myshape", s)
turtle.shape("myshape")

sleep(5)