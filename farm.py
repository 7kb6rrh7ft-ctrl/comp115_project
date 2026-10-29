import turtle
t = turtle.Turtle()
t.speed(0)
def rectangle(x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()
# Grass
rectangle(-350, -250, 700, 250, "green")
# Farm house
rectangle(-150, -80, 160, 120, "red")
# Roof
t.penup()
t.goto(-170, 40)
t.pendown()
t.color("brown")
t.begin_fill()
t.goto(-70, 130)
t.goto(30, 40)
t.goto(-170, 40)
t.end_fill()
# Door
rectangle(-90, -80, 40, 70, "yellow")
# Sun
t.penup()
t.goto(180, 160)
t.dot(80, "gold")
t.hideturtle()
turtle.done()
