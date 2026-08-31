import turtle

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.pencolor("#00ffcc")

for i in range(36):
    t.circle(100)
    t.left(10)
    

t.hideturtle()

screen.mainloop()