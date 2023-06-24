from turtle import *

def init(screen_width=1024, screen_height=1024, line_width=1):
    setup(screen_width, screen_height)
    width(line_width)
    hideturtle()
    tracer(False)

def post_init():
    tracer(True)
    exitonclick()
