from turtle import *
from setup import init, post_init
import random

NOISE_RANGE = 5
SIZE = 100
SHRINK_FACTOR = 15

init()

def draw_square(x, y, size):
    penup()
    goto(x - size * .5, y - size * .5)
    pendown()
    for _ in range(4):
        forward(size)
        left(90)

tiles = range(-500 + SIZE // 2, 500, SIZE)

for x in tiles:
    for y in tiles:
        draw_square(x, y, SIZE)
        x_off = random.uniform(-NOISE_RANGE, NOISE_RANGE)
        y_off = random.uniform(-NOISE_RANGE, NOISE_RANGE)
        for i in range(6):
          draw_square(x + i * x_off, y + i * y_off, SIZE - i * SHRINK_FACTOR)

post_init()
