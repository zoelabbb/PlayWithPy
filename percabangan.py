# Materi if percabangan & Looping

while True:
    print('Menu Pilihan')
    print('1. Cari angka genap')
    print('2. Cari angka ganjil')
    print('3. Convert suhu Celcius > Fahrenheit')
    pilih = int(input('Pilihanmu > '))

    if pilih == 1:
        genap = int(input('Masukkan angka : '))

        hasil = genap % 2

        if hasil == 0:
            print(genap, 'Adalah angka genap')
        else:
            print(genap, 'Bukan angak genap')

    elif pilih == 2:
        ganjil = int(input('Masukkan angka : '))

        hasil = ganjil % 2

        if hasil != 0:
            print(ganjil, 'Adalah angka ganjil')
        else:
            print(ganjil, 'Bukan angak ganjil')
    elif pilih == 3:
        celcius = float(input('Masukkan suhu Celcius : '))
        fahren = (celcius * 9/5) + 32
        print('Suhu fahrenheit : ', fahren)

    else:
        print('Pilihan tidak valid. Silakan pilih angka 1, 2, atau 3.')
        break
