import turtle

# Buat objek Turtle
fibonacci_turtle = turtle.Turtle()

# Setel kecepatan menggambar (opsional)
fibonacci_turtle.speed(0)  # 0 untuk secepat mungkin, Anda bisa mengubahnya

# Fungsi rekursif untuk menggambar pohon Fibonacci
def fibonacci_tree(branch_len, t):
    if branch_len > 5:  # Syarat berhenti rekursif
        # Gambar cabang ke atas
        t.forward(branch_len)
        t.right(20)
        fibonacci_tree(branch_len - 15, t)

        # Kembali ke posisi awal
        t.left(40)
        fibonacci_tree(branch_len - 15, t)

        # Kembali ke posisi awal
        t.right(20)
        t.backward(branch_len)

# Atur posisi awal
fibonacci_turtle.left(90)
fibonacci_turtle.up()
fibonacci_turtle.backward(100)
fibonacci_turtle.down()

# Gambar pohon Fibonacci
fibonacci_tree(100, fibonacci_turtle)

# Tutup jendela grafik Turtle saat di-klik
turtle.done()