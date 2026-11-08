import csv
import os
from datetime import date, timedelta

import requests

URL = "https://api.frankfurter.dev/v1"


def ambil_data(alamat, parameter):
    """Ambil data JSON dari internet. Kalau gagal, tampilkan pesan dan kembalikan None."""
    try:
        respon = requests.get(alamat, params=parameter, timeout=10)
        respon.raise_for_status()
        return respon.json()
    except requests.exceptions.ConnectionError:
        print("Gagal terhubung ke internet. Cek koneksimu lalu coba lagi.")
    except requests.exceptions.Timeout:
        print("Server terlalu lama menjawab. Coba lagi sebentar.")
    except requests.exceptions.HTTPError:
        print("Data tidak ditemukan. Cek kode mata uangnya (contoh: USD, EUR, JPY).")
    except requests.exceptions.RequestException:
        print("Terjadi masalah saat mengambil data.")
    except ValueError:
        print("Jawaban server tidak bisa dibaca.")
    return None


def kurs_hari_ini(asal, tujuan):
    """Kembalikan (kurs, tanggal) untuk 1 satuan mata uang asal ke tujuan."""
    data = ambil_data(f"{URL}/latest", {"base": asal, "symbols": tujuan})
    if data is None or tujuan not in data.get("rates", {}):
        return None, None
    return data["rates"][tujuan], data["date"]


def minta_kode(pesan):
    return input(pesan).strip().upper()


def menu_kurs():
    teks = minta_kode("Mata uang (pisah koma, contoh USD,EUR,JPY): ")
    daftar = [k.strip() for k in teks.split(",") if k.strip()]
    if not daftar:
        print("Belum ada mata uang yang diisi.")
        return
    print("\n" + "=" * 40)
    for kode in daftar:
        kurs, tanggal = kurs_hari_ini(kode, "IDR")
        if kurs is None:
            print(f"{kode:<6} tidak tersedia")
        else:
            print(f"1 {kode:<4} = Rp {kurs:>12,.2f}  ({tanggal})")
    print("=" * 40)


def menu_konversi():
    try:
        jumlah = float(input("Jumlah: ").strip().replace(",", "."))
    except ValueError:
        print("Jumlah harus berupa angka.")
        return
    asal = minta_kode("Dari mata uang (contoh USD): ")
    tujuan = minta_kode("Ke mata uang (Enter untuk IDR): ") or "IDR"
    kurs, tanggal = kurs_hari_ini(asal, tujuan)
    if kurs is None:
        return
    hasil = jumlah * kurs
    print(f"\n{jumlah:,.2f} {asal} = {hasil:,.2f} {tujuan}")
    print(f"(kurs 1 {asal} = {kurs:,.4f} {tujuan}, tanggal {tanggal})")


def menu_riwayat():
    kode = minta_kode("Mata uang (contoh USD): ")
    hari_ini = date.today()
    awal = hari_ini - timedelta(days=30)
    data = ambil_data(f"{URL}/{awal}..{hari_ini}", {"base": kode, "symbols": "IDR"})
    if data is None or not data.get("rates"):
        print("Riwayat tidak tersedia.")
        return

    baris = []
    for tanggal in sorted(data["rates"]):
        baris.append([tanggal, kode, data["rates"][tanggal]["IDR"]])

    nama_file = f"kurs_{kode}.csv"
    try:
        with open(nama_file, "w", newline="", encoding="utf-8") as f:
            penulis = csv.writer(f)
            penulis.writerow(["tanggal", "mata_uang", "kurs"])
            penulis.writerows(baris)
    except PermissionError:
        print("Gagal menyimpan. Tutup dulu file CSV-nya kalau sedang terbuka.")
        return

    print(f"\n{len(baris)} hari tersimpan: {os.path.abspath(nama_file)}")
    print(f"Terendah  : Rp {min(b[2] for b in baris):,.2f}")
    print(f"Tertinggi : Rp {max(b[2] for b in baris):,.2f}")
    print("File ini bisa langsung dibuat grafik dengan grafik_csv.py.")


def main():
    print("=== PENGAMBIL KURS MATA UANG ===")
    print("Data: Bank Sentral Eropa (via Frankfurter), diperbarui tiap hari kerja")
    while True:
        print("\nMenu:")
        print("  1. Kurs hari ini ke rupiah")
        print("  2. Konversi mata uang")
        print("  3. Riwayat 30 hari (simpan ke CSV)")
        print("  0. Keluar")
        menu = input("Pilih menu: ").strip()
        if menu == "1":
            menu_kurs()
        elif menu == "2":
            menu_konversi()
        elif menu == "3":
            menu_riwayat()
        elif menu == "0":
            print("Sampai jumpa")
            break
        else:
            print("Menu tidak valid.")


main()