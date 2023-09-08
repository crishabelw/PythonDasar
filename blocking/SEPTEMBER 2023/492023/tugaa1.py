# Menghitung dan mencetak keliling dan luas persegi
sisi_persegi = float(input("Masukkan panjang sisi persegi: "))
keliling_persegi = 4 * sisi_persegi
luas_persegi = sisi_persegi ** 2
print(f"Keliling persegi: {keliling_persegi}")
print(f"Luas persegi: {luas_persegi}")

# Menghitung dan mencetak keliling dan luas persegi panjang
panjang = float(input("Masukkan panjang persegi panjang: "))
lebar = float(input("Masukkan lebar persegi panjang: "))
keliling_persegi_panjang = 2 * (panjang + lebar)
luas_persegi_panjang = panjang * lebar
print(f"Keliling persegi panjang: {keliling_persegi_panjang}")
print(f"Luas persegi panjang: {luas_persegi_panjang}")

# Menghitung dan mencetak keliling dan luas trapesium
sisi_a = float(input("Masukkan panjang sisi pertama trapesium: "))
sisi_b = float(input("Masukkan panjang sisi kedua trapesium: "))
tinggi = float(input("Masukkan tinggi trapesium: "))
keliling_trapesium = sisi_a + sisi_b + 2 * (sisi_a*2 + sisi_b*2)**0.5
luas_trapesium = 0.5 * (sisi_a + sisi_b) * tinggi
print(f"Keliling trapesium: {keliling_trapesium}")
print(f"Luas trapesium: {luas_trapesium}")
