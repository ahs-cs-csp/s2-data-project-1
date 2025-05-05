from turtle import *
setup(700, 300)
t = Turtle()

def square(x, y, size, color):
    t.fillcolor(...)
    t.begin_fill()
    t.penup()
    t.goto(..., ...)
    t.pendown()
    for i in range(...):
        t.forward(...)
        t.right(...)
    t.end_fill()

def triangle(x, y, size, color):
    t.fillcolor(...)
    t.begin_fill()
    t.penup()
    t.goto(..., ...)
    t.pendown()
    for i in range(...):
        t.forward(...)
        t.right(...)
    t.end_fill()

def draw_house(x, y, size):
    t.penup()
    t.goto(..., ...)
    t.pendown()
    square(..., ..., ..., ...)
    t.right(...)
    # this next line takes some thinking
    triangle(..., ..., ..., ...)
    t.right(...)

# uncomment these to test the functions
# square(0, 0, 100)
# triangle(0, 100, 100)
for i in range(...):
    draw_house(... + (... * ...), 0, 100)
t.screen.mainloop()