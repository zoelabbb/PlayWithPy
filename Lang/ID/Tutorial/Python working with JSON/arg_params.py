# Materi argument with parameter
# Mencetak data dengan file JSON

import json
import os
import module.mymodule as mymodule

# Buat folder json jika not exist
json_folder = 'json'
os.makedirs(json_folder, exist_ok=True)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def cari_angka_genap(angka):
    hasil = angka % 2

    if hasil == 0:
        print(angka, 'Adalah angka genap')
        print('')
    else:
        print(angka, 'Bukan angka genap')
        print('')

def cari_angka_ganjil(angka):
    hasil = angka % 2

    if hasil == 1:
        print(angka, 'Adalah angka ganjil')
        print('')
    else:
        print(angka, 'Bukan angka ganjil')
        print('')

def convert_suhu(celcius):
    fahrenheit = (celcius * 9/5) + 32

    suhu_dict = {
        "Menu" : 'Convert Suhu Celcius to Fahrenheit',
        "Celcius" : celcius,
        "Hasil convert" : fahrenheit,
        "Msg" : mymodule.itsme()
    }
    
    # Menentukan path file dan folder
    json_folder = 'json'  # Ganti dengan path folder yang diinginkan
    json_filename = os.path.join(json_folder, 'hasil.json')

    # Membaca data JSON yang sudah ada (jika ada)
    existing_data = []
    if os.path.exists(json_filename):
        with open(json_filename, 'r') as file:
            try:
                existing_data = json.load(file)
                if not isinstance(existing_data, list):
                    existing_data = []  # Memastikan existing_data is a list
            except json.decoder.JSONDecodeError:
                pass

    # Menambahkan data baru ke dalam data json yang sudah ada
    existing_data.append(suhu_dict)

    # Save file hasil.json ke dalam folder json
    json_filename = os.path.join(json_folder, 'hasil.json')
    with open(json_filename, 'w') as file:
        json.dump(existing_data, file, indent=4)
        
    print('Suhu Fahrenheit:', fahrenheit)
    print('Hasil telah disimpan ke dalam directory', json_filename)
    print('')
    
def cari_genap(look_a, look_b):
    # Menyimpan angka genap antara 1 dan 100 dalam list
    angka_genap = [i for i in range(look_a, look_b + 1) if i % 2 == 0]

    # Menampilkan list angka genap
    print(angka_genap)
    print('')
    
def for_ganjil(for_a, for_b):
    # Mencari angka genap antara 1 dan 100
    for i in range(for_a, for_b ):
        if i % 2 == 1:
            print(i)


while True:
    print('Menu Pilihan')
    print('1. Cek angka genap')
    print('2. Cek angka ganjil')
    print('3. Convert suhu Celcius to Fahrenheit')
    print('4. Cari angka genap [Method List Comprehension]')
    print('5. Cari angka ganjil [Method For]')
    print('q. Keluar')

    print(' ')
    pilih = input('Pilihanmu > ')
    clear_terminal()

    if pilih.lower() == 'q':
        print('Keluar dari program.')
        break

    pilih = int(pilih)

    if pilih == 1:
        angka = int(input('Masukkan angka: '))
        cari_angka_genap(angka)
    elif pilih == 2:
        angka = int(input('Masukkan angka: '))
        cari_angka_ganjil(angka)
    elif pilih == 3:
        celcius = float(input('Masukkan suhu Celcius: '))
        convert_suhu(celcius)
    elif pilih == 4:
        look_a = int(input('Masukkan angka: '))
        look_b = int(input('Masukkan angka: '))
        print('')
        cari_genap(look_a, look_b)
    elif pilih == 5:
        for_a = int(input('Masukkan angka: '))
        for_b = int(input('Masukkan angka: '))
        for_ganjil(for_a, for_b)
        print('')
    else:
        print('Pilihan tidak valid. Silakan pilih angka 1, 2, atau 3.')
        break