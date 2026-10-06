import csv
import os
from models import Buku


def tambah_buku():
    print("=== MENU TAMBAH BUKU ===")
    print("1. Tambah Buku")
    print("0. Keluar")

    pilihan = input("Pilihan: ")

    if pilihan == "1":
        print("\n--- Form Input Data Buku ---")
        judul = input("Judul Buku : ").strip()
        penulis = input("Penulis    : ").strip()
        isbn = input("ISBN       : ").strip()

        # Peringatan / Validasi: Semua kolom harus diisi
        if not judul or not penulis or not isbn:
            print(
                "\n[PERINGATAN] Semua kolom harus diisi! Data gagal disimpan.\n"
            )
            return

        # Membuat objek dari Class Buku (diimpor dari models.py)
        buku_baru = Buku(judul, penulis, isbn)

        file_csv = "buku.csv"
        file_exists = os.path.isfile(file_csv)

        # Proses pembuatan header dan penyimpanan ke file buku.csv
        try:
            with open(file_csv, mode="a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)

                # Jika file belum ada, tulis header terlebih dahulu
                if not file_exists:
                    writer.writerow(["Judul", "Penulis", "ISBN", "Status"])

                # Menulis data buku baru ke file CSV
                writer.writerow(buku_baru.to_list())

            print("\n[BERHASIL] Data buku berhasil ditambahkan ke buku.csv!\n")

        except Exception as e:
            print(f"\n[ERROR] Terjadi kesalahan saat menyimpan data: {e}\n")

    elif pilihan == "0":
        print("Kembali ke menu utama.")
    else:
        print("Pilihan tidak valid!")


if __name__ == "__main__":
    tambah_buku()
