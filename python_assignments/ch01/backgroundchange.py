import turtle
t=turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
colors=["red","orange","purple","blue"]
for x in range(300):
    t.pencolor(colors[ x %4])
    t.circle(x)
    t.left(90)