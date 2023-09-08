import turtle

# Membuat objek turtle
t = turtle.Turtle()

# Fungsi untuk menggambar persegi panjang
def draw_rectangle():
    for _ in range(2):
        t.forward(100)
        t.left(90)
        t.forward(200)
        t.left(90)

# Fungsi untuk menggambar segitiga
def draw_triangle():
    for _ in range(3):
        t.forward(100)
        t.left(120)

# Fungsi untuk menggambar trapesium
def draw_trapezium():
    t.forward(100)
    t.left(45)
    t.forward(50)
    t.left(135)
    t.forward(100)
    t.left(45)
    t.forward(50)

# Fungsi untuk menggambar jajar genjang
def draw_parallelogram():
    t.forward(100)
    t.left(60)
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(60)
    t.forward(100)

# Fungsi untuk menggambar belah ketupat
def draw_rhombus():
    t.left(45)
    for _ in range(4):
        t.forward(100)
        t.left(90)

# Menggambar bangun datar
draw_rectangle()
t.penup()
t.goto(150, 0)
t.pendown()
draw_triangle()
t.penup()
t.goto(-150, -200)
t.pendown()
draw_trapezium()
t.penup()
t.goto(150, -200)
t.pendown()
draw_parallelogram()
t.penup()
t.goto(-150, -400)
t.pendown()
draw_rhombus()

# Menutup jendela setelah selesai
turtle.done()

