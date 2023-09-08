import turtle 

#Gambar lingkarang besar 
turtle.pensize(5)
turtle.bgcolor("white")
turtle.color("black")
turtle.penup()
turtle.goto(40, 10)
turtle.pendown()
turtle.circle(150)

#Gambar lingkaran ditengah 
turtle.color("blue")
turtle.fillcolor("blue")
turtle.begin_fill()
turtle.penup()
turtle.goto(40, 40)
turtle.pendown()
turtle.circle(120)
turtle.end_fill()

#Gambar lingkaran kecil 
turtle.color("white")
turtle.fillcolor("black")
turtle.begin_fill()
turtle.penup()
turtle.goto(3,205)
turtle.pendown()
turtle.circle(20)
turtle.end_fill()

#Gambar tangan 
turtle.color("red")
turtle.fillcolor("red")
turtle.begin_fill()
turtle.penup()
turtle.goto(60, 70)
turtle.pendown()
for _ in range(4):
    turtle.forward(40) 
    turtle.left(90) 
turtle.end_fill()

#lingkaran di tangan
turtle.color("red")
turtle.fillcolor("red")
turtle.begin_fill()
turtle.penup() 
turtle.goto(80,90)
turtle.pendown()
turtle.circle(40)
turtle.end_fill()

#membuat jari kelingking
turtle.color("red")
turtle.fillcolor("red")
turtle.begin_fill()
turtle.penup()
turtle.goto(98,145)
turtle.pendown()
for _ in range(2):  
    turtle.forward(20)
    turtle.left(90)      
    turtle.forward(50)   
    turtle.left(90)   
turtle.end_fill() 

#membuat jari manis 
turtle.color("red")
turtle.fillcolor("red")
turtle.begin_fill()
turtle.penup()
turtle.goto(73,160)
turtle.pendown()
for _ in range(2): 
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(53)
    turtle.left(90)
turtle.end_fill() 

#membuat jari tengah 
turtle.color("red")
turtle.fillcolor("red")
turtle.begin_fill()
turtle.penup()
turtle.goto(53,160)
turtle.pendown()
for _ in range(2): 
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
turtle.end_fill()

#membuat jari telunjuk 
turtle.color("red")
turtle.fillcolor("red")
turtle.begin_fill()
turtle.penup()
turtle.goto(33,150)
turtle.pendown()
for _ in range(2): 
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(80)
    turtle.left(90)
turtle.end_fill()