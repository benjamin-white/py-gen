import turtle as t
import random
from setup import init, post_init

INITIAL_BRANCH_LENGTH = 150
LENGTH_FALLOFF = .8
BRANCHING_ANGLE = 20
NOISE_AMOUNT = 7

def grow(length, falloff, angle, noise=0):
    if length < 10:
        return

    width = length / 20
    t.width(width if width > 1 else 1)
    t.forward(length)
    branch_length = length * falloff
    if noise > 0:
        branch_length *= random.uniform(.9, 1.1)

    angle_left = angle + random.gauss(0, noise)
    angle_right = angle + random.gauss(0, noise)

    t.left(angle_left)
    grow(branch_length, falloff, angle, noise)
    t.right(angle_left)

    t.right(angle_right)
    grow(branch_length, falloff, angle, noise)
    t.left(angle_right)

    t.backward(length)

init()

t.penup()
t.goto(0, -400)
t.pendown()
t.left(90)
grow(INITIAL_BRANCH_LENGTH, LENGTH_FALLOFF, BRANCHING_ANGLE, NOISE_AMOUNT)

post_init()
