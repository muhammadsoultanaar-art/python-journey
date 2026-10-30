import json
from pathlib import Path

FILE = Path(__file__).with_name("keuangan.json")


def muat():
    try:
        with open(FILE) as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def simpan(data):
    with open(FILE, "w") as f:
        json.dump(data, f)


def tambah(data):
    jenis = input("Jenis (masuk/keluar): ")
    if jenis not in ("masuk", "keluar"):
        print("Jenis harus masuk atau keluar")
        return
    kategori = input("Kategori: ")
    try:
        jumlah = int(input("Jumlah: "))
    except ValueError:
        print("Jumlah harus angka")
        return
    data.append({"jenis": jenis, "kategori": kategori, "jumlah": jumlah})
    simpan(data)
    print("Tersimpan")


def riwayat(data):
    print("=" * 36)
    for item in data:
        tanda = "+" if item["jenis"] == "masuk" else "-"
        print(f"{item['kategori']:<18}{tanda}{item['jumlah']:>17,}")
    print("=" * 36)


def ringkasan(data):
    masuk = 0
    keluar = 0
    per_kategori = {}
    for item in data:
        if item["jenis"] == "masuk":
            masuk = masuk + item["jumlah"]
        else:
            keluar = keluar + item["jumlah"]
            kat = item["kategori"]
            per_kategori[kat] = per_kategori.get(kat, 0) + item["jumlah"]
    print("=" * 36)
    print(f"{'Pemasukan':<18}{masuk:>18,}")
    print(f"{'Pengeluaran':<18}{keluar:>18,}")
    print(f"{'Saldo':<18}{masuk - keluar:>18,}")
    print("-" * 36)
    for kat, total in per_kategori.items():
        print(f"{kat:<18}{total:>18,}")
    print("=" * 36)


data = muat()

while True:
    print("1. Tambah  2. Riwayat  3. Ringkasan  0. Keluar")
    menu = input("Pilih menu: ")
    if menu == "1":
        tambah(data)
    elif menu == "2":
        riwayat(data)
    elif menu == "3":
        ringkasan(data)
    elif menu == "0":
        break
    else:
        print("Menu tidak ada")

print("Sampai jumpa")