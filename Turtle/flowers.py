import turtle
import random

def draw_flower():
    turtle.circle(50)
    turtle.circle(25)

turtle.speed(0)
turtle.penup()
turtle.goto(600,400)
turtle.pendown()

for i in range(10):
    turtle.penup()
    turtle.goto(random.randint(-300,300),random.randint(-200,200))
    turtle.pendown()
    draw_flower()

turtle.exitonclick()
