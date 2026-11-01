import csv
from pathlib import Path


def ke_angka(teks):
    bersih = teks.strip().replace("Rp", "").replace(" ", "").replace(",", "")
    if bersih == "":
        return None
    try:
        return float(bersih)
    except ValueError:
        return None


def baca_csv(file):
    for sandi in ["utf-8-sig", "cp1252"]:
        try:
            with open(file, encoding=sandi, newline="") as f:
                contoh = f.read(2048)
                f.seek(0)
                try:
                    pemisah = csv.Sniffer().sniff(contoh, delimiters=",;\t").delimiter
                except csv.Error:
                    pemisah = ","
                pembaca = csv.DictReader(f, delimiter=pemisah)
                baris = list(pembaca)
                return pembaca.fieldnames, baris
        except UnicodeDecodeError:
            continue
    return None, []


def jenis_kolom(kolom, baris):
    terisi = 0
    for b in baris:
        nilai = (b.get(kolom) or "").strip()
        if nilai != "":
            terisi = terisi + 1
            if ke_angka(nilai) is None:
                return "teks"
    if terisi == 0:
        return "kosong"
    return "angka"


def statistik_angka(kolom, baris):
    nilai = []
    for b in baris:
        angka = ke_angka(b.get(kolom) or "")
        if angka is not None:
            nilai.append(angka)
    return len(nilai), sum(nilai), sum(nilai) / len(nilai), min(nilai), max(nilai)


def sering_muncul(kolom, baris, n=5):
    hitung = {}
    for b in baris:
        nilai = (b.get(kolom) or "").strip()
        if nilai != "":
            hitung[nilai] = hitung.get(nilai, 0) + 1
    urut = sorted(hitung.items(), key=lambda p: p[1], reverse=True)
    return urut[:n], len(hitung)


def total_per_kelompok(kolom_teks, kolom_angka, baris):
    total = {}
    for b in baris:
        kunci = (b.get(kolom_teks) or "").strip()
        angka = ke_angka(b.get(kolom_angka) or "")
        if kunci == "" or angka is None:
            continue
        total[kunci] = total.get(kunci, 0) + angka
    return sorted(total.items(), key=lambda p: p[1], reverse=True)


def laporan(nama, kolom, baris):
    teks = []
    teks.append("=" * 60)
    teks.append(f"LAPORAN: {nama}")
    teks.append(f"Jumlah baris: {len(baris):,}   Jumlah kolom: {len(kolom)}")
    teks.append("=" * 60)
    for k in kolom:
        jenis = jenis_kolom(k, baris)
        if jenis == "angka":
            n, total, rata, kecil, besar = statistik_angka(k, baris)
            teks.append(f"[angka] {k}")
            teks.append(f"   total {total:,.0f} | rata-rata {rata:,.2f} | min {kecil:,.0f} | maks {besar:,.0f} | terisi {n}")
        elif jenis == "teks":
            sering, unik = sering_muncul(k, baris)
            teks.append(f"[teks] {k} ({unik} nilai berbeda)")
            for nilai, jumlah in sering:
                potong = nilai[:30]
                teks.append(f"   {potong:<30} {jumlah:>6}")
        else:
            teks.append(f"[kosong] {k}")
    return teks


def pilih_kolom(kolom, baris, jenis, pesan):
    pilihan = []
    for k in kolom:
        if jenis_kolom(k, baris) == jenis:
            pilihan.append(k)
    if len(pilihan) == 0:
        print(f"Tidak ada kolom {jenis}")
        return None
    for nomor, k in enumerate(pilihan, start=1):
        print(f"{nomor}. {k}")
    try:
        nomor = int(input(pesan))
    except ValueError:
        return None
    if 1 <= nomor <= len(pilihan):
        return pilihan[nomor - 1]
    return None


def tampil_total(kolom, baris):
    kolom_teks = pilih_kolom(kolom, baris, "teks", "Kelompokkan berdasarkan nomor: ")
    if kolom_teks is None:
        print("Pilihan tidak valid")
        return
    kolom_angka = pilih_kolom(kolom, baris, "angka", "Jumlahkan kolom nomor: ")
    if kolom_angka is None:
        print("Pilihan tidak valid")
        return
    hasil = total_per_kelompok(kolom_teks, kolom_angka, baris)
    total_semua = 0
    for nama, total in hasil:
        total_semua = total_semua + total
    print("=" * 49)
    for nama, total in hasil:
        persen = 0
        if total_semua != 0:
            persen = total / total_semua * 100
        potong = nama[:24]
        print(f"{potong:<24}{total:>16,.0f}{persen:>8.1f}%")
    print("=" * 49)


def muat_file():
    file = Path(input("Lokasi file CSV: ").strip().strip('"'))
    if not file.is_file():
        print("File tidak ditemukan")
        return None
    kolom, baris = baca_csv(file)
    if not kolom or len(baris) == 0:
        print("File kosong atau tidak terbaca")
        return None
    return file, kolom, baris


sumber = muat_file()
if sumber is not None:
    file, kolom, baris = sumber
    isi = laporan(file.name, kolom, baris)
    print("\n".join(isi))
    while True:
        print("1. Total per kelompok  2. Simpan laporan  3. Tampilkan laporan  0. Keluar")
        menu = input("Pilih menu: ")
        if menu == "1":
            tampil_total(kolom, baris)
        elif menu == "2":
            tujuan = file.with_name(f"laporan_{file.stem}.txt")
            with open(tujuan, "w", encoding="utf-8") as f:
                f.write("\n".join(isi))
            print(f"Disimpan: {tujuan}")
        elif menu == "3":
            print("\n".join(isi))
        elif menu == "0":
            break
        else:
            print("Menu tidak ada")

print("Sampai jumpa")