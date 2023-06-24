import math
import random
import turtle as t
from setup import init, post_init

BOX_SIZE = 20
HALF_CANVAS_SIZE = 400
MAX_DISTANCE = math.sqrt(HALF_CANVAS_SIZE ** 2 + HALF_CANVAS_SIZE * 2)

init(line_width=2)

for y in range(HALF_CANVAS_SIZE, -HALF_CANVAS_SIZE, -BOX_SIZE):
    for x in range(-HALF_CANVAS_SIZE, HALF_CANVAS_SIZE, BOX_SIZE):
        t.penup()
        t.goto(x, y)
        t.pendown()
        distance = math.sqrt(x ** 2 + y ** 2)
        noise_amount = (distance - MAX_DISTANCE)
        angle = random.uniform(-noise_amount, noise_amount) if noise_amount > 5 else 0
        t.right(angle)

        for i in range(4):
            t.forward(BOX_SIZE)
            t.right(90)

        t.left(angle)

post_init()
