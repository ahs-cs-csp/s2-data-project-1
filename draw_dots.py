from turtle import *
import random

setup(500, 300)
t = Turtle()
        # 0       1       2         3
colors = ["red","blue","yellow", "green"]
t.penup()
for i in range(...):
    rand_x = random.randint(..., ...)
    rand_y = random.randint(..., ...)
    rand_size = random.randint(..., ...)
    rand_color_index = random.randint(..., ...) 
    t.goto(rand_x, rand_y)
    t.dot(..., colors[rand_color_index])
t.screen.mainloop()