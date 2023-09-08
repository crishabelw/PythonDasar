while True: 
    nilai = float(input("Masukkan nilai siswa: "))

    if nilai >= 75: 
        print("Siswa tuntas!")
        break 
    else: 
        ulang = input("Nilai kurang dari 75. Apakah ingin menginput ulang? (ya/tidak): ")
        if ulang.lower() != "ya": 
            print("Siswa tidak tuntas.")
            break