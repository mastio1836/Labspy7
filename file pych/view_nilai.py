from model.daftar_nilai import daftar

# Menampilkan data
def lihat_data():
    print("Daftar Nilai:")
    print("___________________________________________________________________")
    print("| No |      Nama      |    NIM    | Tugas |  UTS  |  UAS  | Akhir |")
    print("===================================================================")
    if daftar.keys():
        no = 1
        for tabel in daftar.values():
            print("| {0:2} | {1:14} | {2:9} | {3:5} | {4:5} | {5:5} | {6:5} |".format
                  (no, tabel[0],
                   tabel[1], tabel[2],
                   tabel[3], tabel[4], tabel[5]))
            no += 1
    else:
        print("=========================TIDAK ADA NILAI===========================")
        print("===================================================================")

# Mencari dan menampilkan data
def cari_data():
    print("Mencari daftar nilai: ")
    print("=================================================")
    nama = input("Masukan nama untuk mencari daftar nilai : ")
    if nama in daftar.keys():
        print("Nama {0}, dengan NIM : {1}\n"
              "Nilai Tugas: {2}, UTS: {3}, dan UAS: {4}\n"
              "dan nilai akhir {5}".format(nama, daftar[nama][1],
                                           daftar[nama][2], daftar[nama][3],
                                           daftar[nama][4], daftar[nama][5]))
    else:
        print("'{}' tidak ditemukan.".format(nama))