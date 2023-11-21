# Materi argument

def cari_angka_genap():
    angka = int(input('Masukkan angka: '))
    hasil = angka % 2

    if hasil == 0:
        print(angka, 'Adalah angka genap')
    else:
        print(angka, 'Bukan angka genap')

def cari_angka_ganjil():
    angka = int(input('Masukkan angka: '))
    hasil = angka % 2

    if hasil != 0:
        print(angka, 'Adalah angka ganjil')
    else:
        print(angka, 'Bukan angka ganjil')

def convert_suhu():
    celcius = float(input('Masukkan suhu Celcius: '))
    fahrenheit = (celcius * 9/5) + 32
    print('Suhu', celcius, 'Celcius =', fahrenheit, 'Fahrenheit')

while True:
    print('Menu Pilihan')
    print('1. Cari angka genap')
    print('2. Cari angka ganjil')
    print('3. Convert suhu Celcius to Fahrenheit')
    print('q. Keluar')

    pilih = input('Pilihanmu > ')

    if pilih.lower() == 'q':
        print('Keluar dari program.')
        break

    pilih = int(pilih)

    if pilih == 1:
        cari_angka_genap()
    elif pilih == 2:
        cari_angka_ganjil()
    elif pilih == 3:
        convert_suhu()
    else:
        print('Pilihan tidak valid. Silakan pilih angka 1, 2, atau 3.')
        break
