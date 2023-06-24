from turtle import *
from setup import init, post_init
import random

BOX_SIZE = 50
noise_amount = .0
line_width = 5

init(line_width=line_width)

for y in range(400, -400, -BOX_SIZE):
    for x in range(-400, 400, BOX_SIZE):
        penup()
        goto(x, y)
        pendown()
        angle = random.uniform(-noise_amount, noise_amount)
        right(angle)

        for i in range(4):
            forward(BOX_SIZE)
            right(90)

        left(angle)

    line_width -= .2
    noise_amount += 4.0
    width(line_width)

post_init()
