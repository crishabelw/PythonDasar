import tkinter as tk

def hitung_total():
    harga_barang = float(entry_harga.get())
    jumlah_barang = int(entry_jumlah.get())
    total_harga = harga_barang * jumlah_barang
    label_total.config(text=f"Total Harga: Rp {total_harga:.2f}")

# Membuat window utama
window = tk.Tk()
window.title("Program Kasir Sederhana")

# Membuat label dan entry untuk harga barang
label_harga = tk.Label(window, text="Harga Barang:")
label_harga.pack()
entry_harga = tk.Entry(window)
entry_harga.pack()

# Membuat label dan entry untuk jumlah barang
label_jumlah = tk.Label(window, text="Jumlah Barang:")
label_jumlah.pack()
entry_jumlah = tk.Entry(window)
entry_jumlah.pack()

# Tombol untuk menghitung total harga
button_hitung = tk.Button(window, text="Hitung Total", command=hitung_total)
button_hitung.pack()

# Label untuk menampilkan total harga
label_total = tk.Label(window, text="Total Harga:")
label_total.pack()

# Memulai aplikasi
window.mainloop()


