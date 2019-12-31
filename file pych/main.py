from model.daftar_nilai import *
from view.view_nilai import *

while True:
    print("\n=================================================")
    print("Silahkan masukan perintah terlebih dahulu:")
    perintah = input("(L) Lihat, (T) Tambah, (U) Ubah, \n"
                     "(H) Hapus, (C) Cari, (K) Keluar: ")
    print("=================================================")

    # Keluar
    if perintah.lower() == 'k':
        break

    # Tambah
    elif perintah.lower() == 't':
        tambah_data()

    elif perintah.lower() == 'c':
        cari_data()

    elif perintah.lower() == 'l':
        lihat_data()

    elif perintah.lower() == 'u':
        ubah_data()

    elif perintah.lower() == 'h':
        hapus_data()
    else:
        print("Silahkan masukan perintah terlebih dahulu.")