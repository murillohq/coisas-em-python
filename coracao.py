import math
import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Coração")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.color("#ffb6c1")

# Fórmula da curva do coração
points = []
for degree in range(0, 361):
    angle = math.radians(degree)
    x = 16 * (math.sin(angle) ** 3)
    y = 13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)
    points.append((x, y))

# Desenha vários corações em escala diferente
for scale in range(11, 17):
    pen.penup()
    pen.goto(points[0][0] * scale, points[0][1] * scale)
    pen.pendown()
    for x, y in points[1:]:
        pen.goto(x * scale, y * scale)

pen.penup()
pen.goto(0, -90)
pen.color("white")
pen.write("I love you", align="center", font=("Arial", 18, "bold"))

screen.mainloop()
