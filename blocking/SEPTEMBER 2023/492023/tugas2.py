import math 
#Fungsi untuk menghitung volume tabung 
def volume_tabung(jari_jari, tinggi): 
    return math.pi*jari_jari**2*tinggi 

#Fungsi untuk menghitung volume balok 
def volume_balok(panjang, lebar, tinggi): 
    return panjang * lebar * tinggi 

#Membaca input dari pengguna 
jenis_bangun_ruang = input("Masukkan jenis bangun ruang (tabung / balok): ")

if jenis_bangun_ruang == "tabung": 
    jari_jari = float(input("Masukkan jari-jari tabung: "))
    tinggi_tabung = float(input("Masukkan tinggi tabung: "))
    print(f"Volume tabung: {volume_tabung(jari_jari, tinggi_tabung)}")
elif jenis_bangun_ruang == "balok": 
    panjang_balok = float(input("Masukkan panjang balok: "))
    lebar_balok = float(input("Masukkan lebar balok: "))
    tinggi_balok = float(input("Masukkan tinggi balok: "))
    print(f"Volume balok:{volume_balok(panjang_balok, lebar_balok,tinggi_balok)}")
else:
    print("Jenis bangun urang tidak valid. Silahkan pilih antara tabung atau balok.")
          