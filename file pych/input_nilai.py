# Menginput data
def input_nama():
    global nama
    nama = input("Masukan nama: ")
    return nama


def input_nim():
    global nim
    nim = input("Masukan nim: ")
    return nim


def input_ntugas():
    global n_tugas
    n_tugas = int(input("Masukan nilai tugas: "))
    return n_tugas


def input_nuts():
    global n_UTS
    n_UTS = int(input("Masukan nilai UTS: "))
    return n_UTS


def input_nuas():
    global n_UAS
    n_UAS = int(input("Masukan nilai UAS: "))
    return n_UAS


# Menghitung nilai akhir
def n_akhir():
    global nakhir
    a = n_tugas * 30 / 100
    b = n_UTS * 35 / 100
    c = n_UAS * 35 / 100
    n_akhir = a+b+c
    return n_akhir