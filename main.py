from turtle import *
import random

setup(1000, 1000)

def tiling(x, y, tileSize, depth, mode="straight"):
    if depth == 0:
      if mode == "straight":
        if random.random() < .5:
          penup()
          goto(x, y - tileSize)
          pendown()
          goto(x, y + tileSize)
        else:
          penup()
          goto(x - tileSize, y)
          pendown()
          goto(x + tileSize, y)
      else:
        if random.random() < .5:
          penup()
          goto(x - tileSize, y + tileSize)
          pendown()
          goto(x + tileSize, y - tileSize)
        else:
          penup()
          goto(x - tileSize, y - tileSize)
          pendown()
          goto(x + tileSize, y + tileSize)
    else:
      tileSize *= .5
      depth -= 1
      tiling(x - tileSize, y + tileSize, tileSize, depth, mode)
      tiling(x + tileSize, y + tileSize, tileSize, depth, mode)
      tiling(x - tileSize, y - tileSize, tileSize, depth, mode)
      tiling(x + tileSize, y - tileSize, tileSize, depth, mode)

width(2)
hideturtle()
tracer(False)
tiling(0, 0, 400, 6, "notstragight")
tracer(True)
exitonclick()
