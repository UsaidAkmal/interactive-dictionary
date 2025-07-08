print(f'''


      _ _      _   _       _ _         
     | (_)    | | (_)     (_) |        
   __| |_  ___| |_ ___   ___| |_ _   _ 
  / _` | |/ __| __| \ \ / / | __| | | |
 | (_| | | (__| |_| |\ V /| | |_| |_| |
  \__,_|_|\___|\__|_| \_/ |_|\__|\__, |
                                  __/ |
    learning dictionary with fun  |___/ 
 

''')

user = input("Masukkan nama user: ")

PC = {
    "mobo": input("Apa mobo kamu: "),
    "prossesor": input("Apa prosesor yang kamu inginkan: "),
    "PSU": input("Apa PSU kamu: "),
    "VGA": input("Apa VGA kamu: "),
    "RAM": input("Apa RAM kamu: "),
    "storaged": input("Apa storaged kamu: "),
    "software": {
        "OS": input("Apa sistem operasi yang kamu pilih: "),
        "python": input("Versi Python berapa yang kamu pilih: "),
        "codeEditor": input("Apa kode editor yang kamu pilih: ")
    }
}

print(f'''
Berikut adalah spesifikasi PC yang kamu sudah rakit

    [+] PC {user} spesifikasinya adalah sebagai berikut:
    [+] mobo       : {PC["mobo"]}
    [+] prosesor   : {PC["prossesor"]}
    [+] PSU        : {PC["PSU"]}
    [+] VGA        : {PC["VGA"]}
    [+] RAM        : {PC["RAM"]}
    [+] storaged   : {PC["storaged"]}
    [+] software   :
        [O] OS         : {PC["software"]["OS"]}
        [O] Python     : {PC["software"]["python"]}
        [O] CodeEditor : {PC["software"]["codeEditor"]}
''')

konfirmasi = input("Apakah kamu ingin melanjutkannya? y/N: ").lower()
if konfirmasi == "y":
    print("Baik, kita akan lanjutkan :)")

    monitor = input("Masukkan merk monitor: ")
    PC["monitor"] = monitor

    updateRAM = input("Upgrade RAM ici boss: ")
    if updateRAM:
        PC["RAM"] = updateRAM

    hapusStoraged = input("Buang HDD ganti SSD? y/N: ").lower()
    if hapusStoraged == "y":
        PC.pop("storaged", None)  # Hapus aman

    updateSSD = input("Apa SSD baru mu ici boss? ")
    if updateSSD:
        PC["SSD"] = updateSSD

    # Cetak ulang versi final
    print("\n===== THE GREAT PC HAS BEEN CREATED =====\n")
    print(f'''
    [+] PC {user} spesifikasinya adalah sebagai berikut:
    [+] mobo       : {PC["mobo"]}
    [+] prosesor   : {PC["prossesor"]}
    [+] PSU        : {PC["PSU"]}
    [+] VGA        : {PC["VGA"]}
    [+] RAM        : {PC["RAM"]}
    [+] storaged   : {PC.get("storaged", "Tidak tersedia")}
    [+] SSD        : {PC.get("SSD", "Belum ditambahkan")}
    [+] monitor    : {PC.get("monitor", "Belum ditambahkan")}
    [+] software   :
        [O] OS         : {PC["software"]["OS"]}
        [O] Python     : {PC["software"]["python"]}
        [O] CodeEditor : {PC["software"]["codeEditor"]}
''')

else:
    print("Bye 👋")
