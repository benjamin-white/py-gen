from turtle import *
from setup import init, post_init
import random

INITIAL_TILE_SIZE = 400
RECURSIVE_DEPTH = 6

init(line_width=2)

def tiling(x, y, tile_size, depth):
    if depth == 0:
      penup()
      if random.random() < .5:
        goto(x - tile_size, y + tile_size)
        pendown()
        goto(x + tile_size, y - tile_size)
      else:
        goto(x - tile_size, y - tile_size)
        pendown()
        goto(x + tile_size, y + tile_size)
    else:
      tile_size *= .5
      depth -= 1
      tiling(x - tile_size, y + tile_size, tile_size, depth)
      tiling(x + tile_size, y + tile_size, tile_size, depth)
      tiling(x - tile_size, y - tile_size, tile_size, depth)
      tiling(x + tile_size, y - tile_size, tile_size, depth)

tiling(0, 0, INITIAL_TILE_SIZE, RECURSIVE_DEPTH)
post_init()
