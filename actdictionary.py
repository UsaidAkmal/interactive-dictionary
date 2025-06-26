user = input("Maukan nama user : ")

PC = {
    "mobo" : input("Apa mobo kamu : "),
    "PSU" : input("Apa PSU kamu : "),
    "VGA" : input("Apa VGA kamu : "),
    "RAM" : input("Apa RAM kamu : "),
    "storaged" : input("Apa Storaged kamu : "),
    "software" : {
        "OS" : input("Apa system operasi yang kamu pilih : "),
        "python" : input("Versi python berapa yang kamu pilih : "),
        "codeEditor" : input("Apa kode Editor yang kamu pilih : ")
    }
}

print(f'''
Berikut adalah spesifikasi PC yang kamu sudah rakit

    [+] PC {user} spesifikasinya adalah sebagai berikut:
    [+] mobo : {PC["mobo"]}
    [+] PSU : {PC["PSU"]}
    [+] VGA : {PC["VGA"]}


''')