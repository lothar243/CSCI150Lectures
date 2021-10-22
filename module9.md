# Module 9.1 - Turtle graphics

[YouTube - Computer Science - Drawing with Turtle part 1 (7:03)](https://www.youtube.com/watch?v=K5VHaqT8s_o)

```python
myscreen = turtle.Screen()

myscreen.exitonclick()
```



How can we calculate the amount we need to turn?

* 1 revolution = 360 degrees
* for a triangle, we accomplish this in 3 turns, 360/3 = 120
* for a square, it takes 4 turns, 360/4 = 90
* For a pentagon, there are 5 turns. What angle would we turn each time?
* How about a 5-pointed star?
* Create a 13-pointed star
* Would this work for a 6-pointed star?

Let's start drawing from a lower position

```python
turtle.goto(0, -300)
```

But it draws while it's traveling, so use `turtle.penup()` and `turtle.pendown()`

Play around drawing a grid of shapes (nested for loops)

# Module 9.2 - More Turtle graphics

```python
myscreen.bgcolor("red")
myscreen.colormode(255) # black screen
myturtle.pencolor(120, 120, 0) # rgb designation
help(turtle) # look at begin_fill() and end_fill()
```

[YouTube - TechCave - The Client Server Model (6:13)](https://www.youtube.com/watch?v=L5BlpPU_muY)

