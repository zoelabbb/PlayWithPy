# PlayWithPy
Belajar python.

File :
1. arg_params.py
2. argue.py
3. percabangan.py

pada file `arg_params.py` aku menambahkan fitur agar bisa mencetak hasil nilai convert suhu di JSON.

## Penjelasan Singkat

kode dibawah ini Line 9 - 10 pada file `arg_params.py`, fungsinya adalah membuat folder bernama (json) jika folder belum ada / belum dibuat. Maka otomatis program akan membuat folder yang sudah di tentukan sebelumnya bernama `json`.
````python

Line code : 9 - 10
File : arg_params.py

json_folder = 'json'
os.makedirs(json_folder, exist_ok=True)
````

