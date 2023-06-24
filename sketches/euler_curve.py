import turtle
from setup import init, post_init

def euler_curve(step_size, angle_step, num_steps):
    angle = 0
    for i in range(num_steps):
        turtle.right(angle)
        turtle.forward(step_size)
        angle += angle_step

init()
euler_curve(step_size=4, angle_step=1.99, num_steps=10000)
post_init()
