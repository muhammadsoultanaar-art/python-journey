import csv
import os

from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

FONT = "Arial"
HEADER_FILL = PatternFill("solid", fgColor="1F4E78")
HEADER_FONT = Font(name=FONT, bold=True, color="FFFFFF")
BIASA = Font(name=FONT)
TEBAL = Font(name=FONT, bold=True)
JUDUL = Font(name=FONT, bold=True, size=14)
GARIS = Border(bottom=Side(style="thin", color="999999"))
FORMAT_ANGKA = "#,##0"
FORMAT_DESIMAL = "#,##0.00"
FORMAT_PERSEN = "0.0%"


def baca_csv(lokasi):
    with open(lokasi, newline="", encoding="utf-8-sig") as f:
        isi = f.read()
    baris_pertama = isi.splitlines()[0] if isi else ""
    pemisah = ";" if baris_pertama.count(";") > baris_pertama.count(",") else ","
    data = list(csv.reader(isi.splitlines(), delimiter=pemisah))
    data = [b for b in data if any(sel.strip() for sel in b)]
    if len(data) < 2:
        return None, None
    header = [h.strip() for h in data[0]]
    baris = []
    for b in data[1:]:
        b = [sel.strip() for sel in b]
        b = (b + [""] * len(header))[: len(header)]
        baris.append(b)
    return header, baris


def ke_angka(teks):
    """Ubah teks jadi angka. Kalau bukan angka, kembalikan None."""
    if teks == "":
        return None
    try:
        nilai = float(teks)
    except ValueError:
        return None
    return int(nilai) if nilai == int(nilai) else nilai


def kolom_angka(header, baris):
    """Nomor kolom yang semua isinya (yang tidak kosong) berupa angka."""
    hasil = []
    for i in range(len(header)):
        isi = [b[i] for b in baris if b[i] != ""]
        if isi and all(ke_angka(x) is not None for x in isi):
            hasil.append(i)
    return hasil


def pilih_nomor(pesan, pilihan):
    while True:
        jawab = input(pesan).strip()
        if jawab.isdigit() and 1 <= int(jawab) <= len(pilihan):
            return pilihan[int(jawab) - 1]
        print("Pilihan tidak valid, coba lagi.")


def tulis_header(ws, baris, daftar):
    for kol, teks in enumerate(daftar, start=1):
        c = ws.cell(row=baris, column=kol, value=teks)
        c.font = HEADER_FONT
        c.fill = HEADER_FILL
        c.alignment = Alignment(horizontal="center")


def buat_sheet_data(wb, header, baris, idx_angka):
    ws = wb.active
    ws.title = "Data"
    tulis_header(ws, 1, header)
    for r, b in enumerate(baris, start=2):
        for k, sel in enumerate(b, start=1):
            if (k - 1) in idx_angka:
                nilai = ke_angka(sel)
                c = ws.cell(row=r, column=k, value=nilai)
                c.number_format = FORMAT_ANGKA
            else:
                c = ws.cell(row=r, column=k, value=sel)
            c.font = BIASA
    for k, h in enumerate(header, start=1):
        terpanjang = max([len(h)] + [len(b[k - 1]) for b in baris])
        ws.column_dimensions[get_column_letter(k)].width = min(terpanjang + 4, 40)
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = f"A1:{get_column_letter(len(header))}{len(baris) + 1}"
    return ws


def buat_sheet_ringkasan(wb, nama_file, header, baris, idx_angka, idx_kel, idx_jum):
    ws = wb.create_sheet("Ringkasan")
    akhir = len(baris) + 1  # baris terakhir di sheet Data

    ws["A1"] = f"Laporan: {nama_file}"
    ws["A1"].font = JUDUL
    ws["A3"] = "Jumlah baris data"
    ws["A3"].font = TEBAL
    ws["B3"] = f"=ROWS(Data!A2:A{akhir})"
    ws["B3"].font = BIASA
    ws["B3"].number_format = FORMAT_ANGKA
    ws["A4"] = "Jumlah kolom"
    ws["A4"].font = TEBAL
    ws["B4"] = len(header)
    ws["B4"].font = BIASA

    # Statistik tiap kolom angka (semuanya rumus, jadi ikut berubah kalau Data diedit)
    r = 6
    ws.cell(row=r, column=1, value="Statistik kolom angka").font = TEBAL
    r += 1
    tulis_header(ws, r, ["Kolom", "Total", "Rata-rata", "Minimum", "Maksimum"])
    for i in idx_angka:
        r += 1
        huruf = get_column_letter(i + 1)
        rentang = f"Data!{huruf}2:{huruf}{akhir}"
        ws.cell(row=r, column=1, value=header[i]).font = BIASA
        rumus = [f"=SUM({rentang})", f"=AVERAGE({rentang})", f"=MIN({rentang})", f"=MAX({rentang})"]
        for k, f in enumerate(rumus, start=2):
            c = ws.cell(row=r, column=k, value=f)
            c.font = BIASA
            c.number_format = FORMAT_DESIMAL if k == 3 else FORMAT_ANGKA

    # Total per kelompok
    total = {}
    for b in baris:
        nilai = ke_angka(b[idx_jum]) or 0
        total[b[idx_kel]] = total.get(b[idx_kel], 0) + nilai
    urutan = sorted(total, key=total.get, reverse=True)  # urutan tampil saja

    r += 2
    ws.cell(row=r, column=1, value=f"Total {header[idx_jum]} per {header[idx_kel]}").font = TEBAL
    r += 1
    tulis_header(ws, r, [header[idx_kel], "Total", "Persen"])
    awal = r + 1
    akhir_kel = awal + len(urutan) - 1
    kel_huruf = get_column_letter(idx_kel + 1)
    jum_huruf = get_column_letter(idx_jum + 1)
    for nama in urutan:
        r += 1
        ws.cell(row=r, column=1, value=nama if nama != "" else "(kosong)").font = BIASA
        kriteria = f"A{r}" if nama != "" else '""'
        c = ws.cell(
            row=r,
            column=2,
            value=f"=SUMIF(Data!${kel_huruf}$2:${kel_huruf}${akhir},{kriteria},Data!${jum_huruf}$2:${jum_huruf}${akhir})",
        )
        c.font = BIASA
        c.number_format = FORMAT_ANGKA
        p = ws.cell(row=r, column=3, value=f"=IF(B{akhir_kel + 1}=0,0,B{r}/B{akhir_kel + 1})")
        p.font = BIASA
        p.number_format = FORMAT_PERSEN
    r += 1
    ws.cell(row=r, column=1, value="Total").font = TEBAL
    t = ws.cell(row=r, column=2, value=f"=SUM(B{awal}:B{akhir_kel})")
    t.font = TEBAL
    t.number_format = FORMAT_ANGKA
    for k in range(1, 4):
        ws.cell(row=r, column=k).border = GARIS

    # Grafik batang
    grafik = BarChart()
    grafik.type = "col"
    grafik.title = f"{header[idx_jum]} per {header[idx_kel]}"
    grafik.y_axis.title = header[idx_jum]
    grafik.x_axis.title = header[idx_kel]
    grafik.legend = None
    grafik.add_data(Reference(ws, min_col=2, min_row=awal - 1, max_row=akhir_kel), titles_from_data=True)
    grafik.set_categories(Reference(ws, min_col=1, min_row=awal, max_row=akhir_kel))
    grafik.height = 8
    grafik.width = 14
    ws.add_chart(grafik, "G3")

    ws.column_dimensions["A"].width = 32
    for huruf in "BCDE":
        ws.column_dimensions[huruf].width = 16
    return ws


def main():
    print("=== PEMBUAT LAPORAN EXCEL ===")
    lokasi = input("Lokasi file CSV: ").strip().strip('"')
    if not os.path.isfile(lokasi):
        print("File tidak ditemukan.")
        return

    header, baris = baca_csv(lokasi)
    if header is None:
        print("File kosong atau hanya berisi header.")
        return

    idx_angka = kolom_angka(header, baris)
    if not idx_angka:
        print("Tidak ada kolom angka. Kalau angkanya berformat 'Rp 1.500.000', bersihkan dulu dengan bersihkan_csv.py.")
        return
    idx_teks = [i for i in range(len(header)) if i not in idx_angka]
    if not idx_teks:
        print("Tidak ada kolom teks untuk dikelompokkan.")
        return

    print("\nKolom teks (untuk dikelompokkan):")
    for n, i in enumerate(idx_teks, start=1):
        print(f"  {n}. {header[i]}")
    idx_kel = pilih_nomor("Pilih nomor kolom kelompok: ", idx_teks)

    print("\nKolom angka (untuk dijumlahkan):")
    for n, i in enumerate(idx_angka, start=1):
        print(f"  {n}. {header[i]}")
    idx_jum = pilih_nomor("Pilih nomor kolom yang dijumlahkan: ", idx_angka)

    nama_file = os.path.basename(lokasi)
    wb = Workbook()
    buat_sheet_data(wb, header, baris, idx_angka)
    buat_sheet_ringkasan(wb, nama_file, header, baris, idx_angka, idx_kel, idx_jum)
    wb.move_sheet("Ringkasan", offset=-1)
    wb.active = 0

    dasar, _ = os.path.splitext(lokasi)
    hasil = dasar + "_laporan.xlsx"
    try:
        wb.save(hasil)
    except PermissionError:
        print("Gagal menyimpan. Tutup dulu file Excel-nya kalau sedang terbuka, lalu coba lagi.")
        return
    print(f"\nLaporan tersimpan: {hasil}")
    print(f"Isi: sheet Ringkasan ({len(baris)} baris data) dan sheet Data.")


main()