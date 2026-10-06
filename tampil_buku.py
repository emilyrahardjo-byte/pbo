import csv
import os
from models import Buku


def muat_data():
    daftar_buku = []
    file_path = "buku.csv"

    if os.path.exists(file_path):
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader, None)  # Lewati header

            for row in reader:
                if row:
                    buku = Buku(row[0], row[1], row[2], row[3])
                    daftar_buku.append(buku)
    else:
        print("File buku.csv tidak ditemukan.")

    return daftar_buku


def tampilkan_buku():
    daftar_buku = muat_data()

    if not daftar_buku:
        print("Tidak ada data buku.")
        return

    print("=" * 35)
    print("DAFTAR BUKU PERPUSTAKAAN")
    print("=" * 35)

    for buku in daftar_buku:
        print(f"Judul   : {buku.judul}")
        print(f"Penulis : {buku.penulis}")
        print(f"ISBN    : {buku.isbn}")
        print(f"Status  : {buku.status}")
        print("-" * 35)

    print("=" * 35)
    print(f"Total Buku: {len(daftar_buku)}")
    print("=" * 35)


def main():
    while True:
        print("\n==================================")
        print("======== SISTEM PERPUSTAKAAN ========")
        print("==================================")
        print("1. Tambah Buku")
        print("2. Tampilkan Buku")
        print("0. Keluar")
        print("==================================")

        pilihan = input("PILIH menu: ")

        if pilihan == "1":
            print("Fitur Tambah Buku belum dipanggil.")
        elif pilihan == "2":
            print("\nData dimuat ulang...\n")
            tampilkan_buku()
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
    