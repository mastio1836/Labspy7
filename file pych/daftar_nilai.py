from view.input_nilai import *

daftar = {}


# Menambahkan data
def tambah_data():
    global daftar
    nama = input_nama()
    nim = input_nim()
    n_tugas = input_ntugas()
    n_UTS = input_nuts()
    n_UAS = input_nuas()
    n_akhir = nakhir()
    daftar[nama] = [nama, nim, n_tugas, n_UTS, n_UAS, n_akhir]
    return daftar


# Mengubah data
def ubah_data():
    print("Masukan data mahasiswa")
    print("...")
    nama = input("Masukan nama untuk mengubah data: ")
    if nama in daftar.keys():
        print("Masukan data yang ingin di ubah :")
        data = input("(Semua), (NIM), "
                     "(Tugas), (UTS), (UAS) : ")
        if data.lower() == "semua":
            print("==========================")
            print("Ubah data {}.".format(nama))
            print("==========================")
            daftar[nama][1] = input("Edit NIM:")
            daftar[nama][2] = int(input("Edit Nilai Tugas: "))
            daftar[nama][3] = int(input("Edit Nilai UTS: "))
            daftar[nama][4] = int(input("Edit Nilai UAS: "))
            # print(daftar)
        elif data.lower() == "nim":
            daftar[nama][1] = input("NIM:")
        elif data.lower() == "tugas":
            daftar[nama][2] = int(input("Nilai Tugas: "))
        elif data.lower() == "uts":
            daftar[nama][3] = int(input("Nilai UTS: "))
        elif data.lower() == "uas":
            daftar[nama][4] = int(input("Nilai UAS: "))
        else:
            print("Perintah tidak ditemukan.")

    else:
        print("'{}' tidak ditemukan.".format(nama))


# Menghapus data
def hapus_data():
    nama = input("Masukan nama untuk menghapus data : ")
    if nama in daftar.keys():
        del daftar[nama]
        print("Data '{}' dihapus.".format(nama))
    else:
        print("'{}' tidak ditemukan.".format(nama))