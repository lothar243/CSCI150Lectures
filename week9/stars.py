import turtle
myscreen = turtle.Screen()
numturns = 7
numrotations = 3
angle = numrotations * 360 / numturns

turtle.color("black", "red")
turtle.begin_fill()
for _ in range(numturns):
    turtle.forward(200)
    turtle.left(angle)
turtle.end_fill()



myscreen.exitonclick()
