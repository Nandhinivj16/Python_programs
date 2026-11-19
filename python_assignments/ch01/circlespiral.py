import turtle
t=turtle.Turtle()
t.speed(0)
colors = ["red","pink","green","yellow"]
for x in range(200):
     t.pencolor(colors [x % 4] )
     t.circle(2*x)
     t.left(90)