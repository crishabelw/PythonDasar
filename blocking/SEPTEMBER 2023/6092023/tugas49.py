import turtle 

def draw_pentagon(side_length): 
    for _ in range(5): 
        turtle.forward(side_length)
        turtle.left(72)

def draw_rectangle(width,height):
    turtle.fillcolor("red")
    turtle.begin_fill()
    for _ in range(2): 
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

def draw_triangle(side_length):
    for _ in range(3):
        turtle.forward(side_length)
        turtle.left(120)

def draw_trapezium(base1, base2, height): 
    turtle.forward(base1)
    turtle.left(135)
    turtle.forward(height)
    turtle.left(45)
    turtle.forward(base2)
    turtle.left(45)
    turtle.forward(height)
    turtle.left(135)
    turtle.forward(base1)
    turtle.forward(base2)

def jajargen(base, height): 
    turtle.forward(base)
    turtle.left(60)
    turtle.forward(height)
    turtle.left(120)
    turtle.forward(base)
    turtle.left(60)
    turtle.forward(height)

turtle.speed(5)

turtle.fillcolor("purple")
turtle.begin_fill()
draw_pentagon(100)
turtle.end_fill()

turtle.penup()
turtle.goto(150, 0)
turtle.pendown()

turtle.fillcolor("red")
turtle.begin_fill()
draw_rectangle(100, 50)
turtle.end_fill()

turtle.penup() 
turtle.goto(-190, 0)
turtle.pendown() 

turtle.fillcolor("yellow")
turtle.begin_fill() 
draw_triangle(100) 
turtle.end_fill()

turtle.penup()
turtle.goto(-150, -100)
turtle.pendown()

turtle.fillcolor("green")
turtle.goto(-150, -100)
turtle.pendown() 

turtle.fillcolor("green")
turtle.begin_fill()
draw_trapezium(100, 200, 80)
turtle.end_fill()

turtle.penup()
turtle.goto(150, -100)
turtle.pendown() 

turtle.color("red")
turtle.fillcolor("blue")
turtle.begin_fill()
jajargen(100, 50)
turtle.end_fill()

turtle.exitonclick()
