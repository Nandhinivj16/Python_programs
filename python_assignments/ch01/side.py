import turtle
t=turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
sides = 3 
colors=["red","orange","purple","blue","green"]
for x in range(360):
    t.pencolor(colors[ x % sides])
    t.forward(x * 3 / sides + x )
    t.left(360/sides + 1)#t.left(360/sides + 2)
    t.width(x*sides/100)
    t.left(90)
