import json

try:
    with open("kontak.json") as f:
        kontak = json.load(f)
except FileNotFoundError:
    kontak = {}

while True:
    print("1. Tambah  2. Cari  3. Lihat semua  0. Keluar")
    menu = input("Pilih menu: ")

    if menu == "1":
        nama = input("Nama: ")
        nomor = input("Nomor: ")
        kontak[nama] = nomor
        with open("kontak.json", "w") as f:
            json.dump(kontak, f)
        print("Kontak disimpan")
    elif menu == "2":
        nama = input("Cari nama: ")
        if nama in kontak:
            print(f"{nama}: {kontak[nama]}")
        else:
            print("Tidak ditemukan")
    elif menu == "3":
        print("=" * 30)
        for nama, nomor in kontak.items():
            print(f"{nama:<15}{nomor:>15}")
        print("=" * 30)
    elif menu == "0":
        break
    else:
        print("Menu tidak ada")

print("Sampai jumpa")