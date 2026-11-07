# python-journey

Catatan dan latihan belajar Python dari nol: dari dasar sampai proyek AI dan game.
Setiap file di repo ini adalah satu program kecil yang bisa langsung dijalankan.

## Cara menjalankan

1. Pasang [Python 3](https://www.python.org/downloads/).
2. Unduh file `.py` yang diinginkan dari repo ini.
3. Buka terminal di folder file tersebut, lalu ketik:

```
python nama_file.py
```

Kalau `python` tidak dikenali, coba `py nama_file.py`. File juga bisa dibuka di VS Code lalu dijalankan dengan tombol **Run**.

## Daftar proyek

| No | File | Fungsi | Konsep utama |
|---|---|---|---|
| 1 | [calculator_struk.py](#1-calculator_strukpy) | Struk belanja satu barang dengan diskon otomatis | `input`, `if`/`else`, f-string |
| 2 | [struk_multi_barang.py](#2-struk_multi_barangpy) | Struk untuk banyak barang | `while` |
| 3 | [struk_diskon_bertingkat.py](#3-struk_diskon_bertingkatpy) | Diskon bertingkat berdasarkan total belanja | `elif` |
| 4 | [tebak_angka.py](#4-tebak_angkapy) | Game tebak angka 1-100 | `random`, `while` |
| 5 | [struk_daftar_barang.py](#5-struk_daftar_barangpy) | Struk yang merinci tiap barang | `list`, `for` |
| 6 | [buku_kontak.py](#6-buku_kontakpy) | Buku kontak dengan menu | `dictionary`, `break` |
| 7 | [kontak_tersimpan.py](#7-kontak_tersimpanpy) | Buku kontak yang datanya tersimpan di file | file JSON, `try`/`except` |
| 8 | [chatbot.py](#8-chatbotpy) | Chatbot berbasis kata kunci | fungsi (`def`, `return`) |
| 9 | [keuangan.py](#9-keuanganpy) | Pencatat pemasukan dan pengeluaran | fungsi, JSON, list berisi dictionary |
| 10 | [alat_kalkulus.py](#10-alat_kalkuluspy) | Pengecek jawaban Kalkulus 1 | `eval`, `None`, komposisi fungsi |
| 11 | [analisis_csv.py](#11-analisis_csvpy) | Penganalisis file CSV otomatis | `csv`, mengelompokkan data |
| 12 | [bersihkan_csv.py](#12-bersihkan_csvpy) | Pembersih data CSV yang berantakan | `set`, `split`/`join`, `DictWriter` |
| 13 | [Laporan excel.py](#13-laporan-excelpy) | Pembuat laporan Excel otomatis dari CSV | `openpyxl`, rumus Excel, grafik |

---

## 1. calculator_struk.py

**Fungsi:** menghitung struk belanja satu jenis barang. Diskon 10% otomatis kalau total belanja 100.000 atau lebih.

**Cara pakai:**
1. Jalankan programnya.
2. Isi harga satuan dan jumlah barang.
3. Struk tampil dengan total, diskon, dan jumlah yang harus dibayar.

**Contoh (harga 50000, jumlah 3):**

```
=======================
         STRUK
=======================
Harga    :       50,000
Jumlah   :            3
Total    :      150,000
Diskon   :          10%
Bayar    :      135,000
=======================
```

---

## 2. struk_multi_barang.py

**Fungsi:** seperti proyek 1, tetapi bisa memasukkan banyak barang dalam satu struk.

**Cara pakai:**
1. Isi harga dan jumlah barang.
2. Jawab `y` pada "tambah barang lagi?" untuk menambah barang, atau `n` untuk selesai.
3. Struk tampil dengan total, diskon 10% (kalau total 100.000 atau lebih), dan jumlah yang harus dibayar.

**Contoh (20000 x 2, lalu 80000 x 1):**

```
=======================
         STRUK
=======================
Total    :      120,000
Diskon   :          10%
Bayar    :      108,000
=======================
```

---

## 3. struk_diskon_bertingkat.py

**Fungsi:** struk banyak barang dengan diskon bertingkat.

| Total belanja | Diskon |
|---|---|
| 100.000 atau lebih | 20% |
| 50.000 sampai 99.999 | 10% |
| di bawah 50.000 | 0% |

**Cara pakai:** sama dengan proyek 2.

**Contoh (total 500.000):**

```
=======================
         STRUK
=======================
Total    :      500,000
Diskon   :          20%
Bayar    :      400,000
=======================
```

**Catatan:** urutan `if`/`elif` penting. Batas terbesar harus ditulis paling atas.

---

## 4. tebak_angka.py

**Fungsi:** komputer memilih angka rahasia 1 sampai 100, pemain menebak sampai benar. Program memberi petunjuk "terlalu kecil" atau "terlalu besar" dan menghitung jumlah percobaan.

**Cara pakai:**
1. Jalankan programnya.
2. Ketik tebakan, lalu tekan Enter.
3. Ulangi sampai tebakan benar.

**Contoh:**

```
tebak angka (1-100): 50
terlalu kecil
tebak angka (1-100): 75
terlalu besar
tebak angka (1-100): 62
benar! kamu butuh 3 percobaan
```

**Tips:** tebak selalu di tengah rentang. Angka 1 sampai 100 paling lama ketemu dalam 7 percobaan.

---

## 5. struk_daftar_barang.py

**Fungsi:** struk yang menampilkan rincian tiap barang (nama, jumlah, subtotal), lengkap dengan diskon bertingkat.

**Cara pakai:**
1. Isi nama barang, harga, dan jumlah.
2. Jawab `y` untuk menambah barang, atau `n` untuk selesai.
3. Struk rinci tampil.

**Contoh (Kopi 15000 x 2, Roti 8000 x 3):**

```
==============================
            STRUK
==============================
Kopi             2      30,000
Roti             3      24,000
==============================
Total                   54,000
Diskon                     10%
Bayar                   48,600
==============================
```

---

## 6. buku_kontak.py

**Fungsi:** buku kontak sederhana dengan menu.

| Menu | Fungsi |
|---|---|
| `1` | Tambah kontak (nama dan nomor) |
| `2` | Cari kontak berdasarkan nama |
| `3` | Lihat semua kontak |
| `0` | Keluar |

**Contoh:**

```
Pilih menu: 1
Nama: Budi
Nomor: 08123
Kontak disimpan
Pilih menu: 2
Cari nama: Budi
Budi: 08123
```

**Catatan:** kontak hanya tersimpan selama program berjalan dan hilang saat program ditutup. Pencarian membedakan huruf besar dan kecil.

---

## 7. kontak_tersimpan.py

**Fungsi:** buku kontak seperti proyek 6, tetapi datanya **tersimpan di file** `kontak.json`, jadi tidak hilang saat program ditutup.

**Cara pakai:** menunya sama dengan `buku_kontak.py` (`1` tambah, `2` cari, `3` lihat semua, `0` keluar). Setiap kontak ditambahkan, data langsung ditulis ke file.

**Contoh:**

```
Pilih menu: 1
Nama: Budi
Nomor: 08123
Kontak disimpan
Pilih menu: 0
Sampai jumpa
```

Jalankan lagi, pilih menu `3`:

```
==============================
Budi                      08123
==============================
```

**Catatan:** `kontak.json` dibuat di folder tempat program dijalankan dan berisi data pribadi, jadi tidak boleh diunggah ke repo.

---

## 8. chatbot.py

**Fungsi:** chatbot yang menjawab berdasarkan kata kunci di dalam pesan.

| Kata kunci | Jawaban |
|---|---|
| `halo` | Sapaan |
| `diskon` | Menanyakan total belanja, lalu menghitung diskonnya |
| `bye` | Salam perpisahan |
| lainnya | "Maaf, aku belum paham." |

**Cara pakai:** ketik pesan lalu Enter. Ketik `keluar` untuk berhenti.

**Contoh:**

```
kamu: halo
bot= halo! ada yang bisa dibantu?
kamu: diskon
total belanja: 120000
bot= diskon kamu 20%
kamu: keluar
```

---

## 9. keuangan.py

**Fungsi:** mencatat pemasukan dan pengeluaran, lalu menghitung saldo dan total pengeluaran per kategori. Data tersimpan di `keuangan.json` (di folder yang sama dengan program).

| Menu | Fungsi |
|---|---|
| `1` | Tambah transaksi (jenis masuk/keluar, kategori, jumlah) |
| `2` | Lihat riwayat transaksi |
| `3` | Ringkasan: pemasukan, pengeluaran, saldo, dan pengeluaran per kategori |
| `0` | Keluar |

**Contoh ringkasan:**

```
====================================
Pemasukan                    1,500,000
Pengeluaran                     35,000
Saldo                        1,465,000
------------------------------------
makan                           35,000
====================================
```

**Catatan:** jumlah yang bukan angka dan jenis selain `masuk`/`keluar` ditolak tanpa menutup program. `keuangan.json` berisi data pribadi, jadi tidak boleh diunggah ke repo.

---

## 10. alat_kalkulus.py

**Fungsi:** alat bantu **mengecek jawaban** Kalkulus 1. Program menghitung dari rumus yang diketik, bukan menggantikan langkah pengerjaan.

| Menu | Fungsi |
|---|---|
| `1` | Tabel nilai f(x), sekaligus menunjukkan domain (nilai yang tidak terdefinisi) |
| `2` | Komposisi fungsi (f o g)(x) dan (g o f)(x) |
| `3` | Mencari bilangan bulat yang memenuhi pertidaksamaan atau nilai mutlak |
| `4` | Menguji tebakan fungsi invers |

**Cara menulis rumus:**
- Perkalian harus eksplisit: `2*x`, bukan `2x`
- Pangkat: `x**2`, akar: `sqrt(x)`, nilai mutlak: `abs(x)`
- Gabungan syarat: `x > 1 and x < 5`
- Ketik hanya ekspresinya (misalnya `x+1`), tanpa `f(x) =` dan tanpa `=`

**Contoh:**

```
f(x) = x+1
g(x) = x**2
x = 3
(f o g)(3.0) = 10.0
(g o f)(3.0) = 16.0
```

```
Pertidaksamaan: abs(x-2) < 3
Bilangan bulat -20..20 yang memenuhi: [0, 1, 2, 3, 4]
```

**Batasan:**
- Pengujian titik hanya indikasi, bukan pembuktian.
- Menu 3 hanya mengecek bilangan bulat -20 sampai 20.
- Program memakai `eval`, jadi hanya untuk rumus yang diketik sendiri. Jangan dipakai untuk teks dari orang lain.

---

## 11. analisis_csv.py

**Fungsi:** membuat laporan otomatis dari file CSV apa pun.
- Jumlah baris dan kolom
- Statistik kolom angka: total, rata-rata, minimum, maksimum
- Nilai yang paling sering muncul di kolom teks
- Total per kelompok (mirip pivot table)
- Laporan bisa disimpan ke file teks

Mendukung CSV dengan pemisah koma atau titik koma (format Excel Indonesia).

**Cara pakai:**
1. Siapkan file CSV (dari Excel: **Save As**, lalu pilih **CSV**), atau pakai data contoh di bawah.
2. Jalankan programnya, lalu masukkan lokasi lengkap file CSV (di Windows: klik file, tekan **Ctrl + Shift + C**, lalu tempel).
3. Laporan tampil. Pilih menu untuk melihat total per kelompok atau menyimpan laporan.

**Data contoh:** salin ke Notepad, lalu simpan sebagai `penjualan.csv` (pada **Save as type**, pilih **All files**).

```
tanggal,produk,kategori,jumlah,harga
2026-10-01,Kopi Susu,Minuman,10,18000
2026-10-01,Roti Bakar,Makanan,5,15000
2026-10-02,Teh Manis,Minuman,8,8000
2026-10-02,Kopi Susu,Minuman,12,18000
2026-10-03,Nasi Goreng,Makanan,6,22000
2026-10-03,Teh Manis,Minuman,15,8000
```

**Contoh hasil menu "Total per kelompok"** (kelompok `kategori`, jumlahkan `jumlah`):

```
=================================================
Minuman                                       45    80.4%
Makanan                                       11    19.6%
=================================================
```

**Batasan:** angka berformat `1.500.000` belum didukung (bersihkan dulu dengan [bersihkan_csv.py](#12-bersihkan_csvpy)), dan total hanya untuk satu kolom angka.

---

## 12. bersihkan_csv.py

**Fungsi:** merapikan data CSV yang berantakan sebelum dianalisis, lalu menyimpan hasilnya sebagai file baru. **File asli tidak diubah.**

Yang dilakukan:
- Merapikan spasi berlebih
- Mengubah angka berformat Indonesia (`Rp 1.250.000`, `Rp 2.500.000`) menjadi angka standar
- Menyeragamkan huruf (Title Case) pada kolom yang dipilih
- Membuang baris kosong
- Membuang baris duplikat
- Menampilkan laporan jumlah perubahan dan pratinjau sebelum/sesudah

**Cara pakai:**
1. Jalankan programnya, lalu masukkan lokasi lengkap file CSV.
2. Jawab `y` kalau kolom angka yang terdeteksi mau diubah ke angka standar.
3. Pilih nomor kolom yang hurufnya mau dirapikan (pisahkan dengan koma, misalnya `1,2`), atau tekan Enter untuk melewati.
4. Periksa laporan dan pratinjau, lalu jawab `y` untuk menyimpan sebagai `namafile_bersih.csv`.

**Data contoh:** salin ke Notepad, lalu simpan sebagai `data_kotor.csv` (pada **Save as type**, pilih **All files**). Spasi di awal dan akhir ` budi santoso ` memang disengaja.

```
nama,kota,tanggal,jumlah,harga
 budi santoso ,JAKARTA,2026-10-01,2,Rp 15.000
siti aminah,bandung,2026-10-01,1,"Rp 1.250.000"
budi santoso,jakarta,2026-10-01,2,15000
,,,,
Andi   Wijaya,surabaya,2026-10-02,3,"Rp 2.500.000"
Siti  Aminah,Bandung,2026-10-01,1,"Rp 1.250.000"
dewi lestari,MEDAN,2026-10-03,,"Rp 75.000"
```

**Contoh hasil** (jawab `y` untuk angka, lalu `1,2` untuk huruf pada kolom `nama` dan `kota`):

```
========================================
Baris awal                  : 7
Sel dirapikan (spasi)       : 3
Angka diubah (jumlah)       : 0
Angka diubah (harga)        : 5
Huruf diubah                : 9
Baris kosong dibuang        : 1
Duplikat dibuang            : 2
Baris akhir                 : 4
========================================
```

Data bersihnya:

```
nama | kota | tanggal | jumlah | harga
Budi Santoso | Jakarta | 2026-10-01 | 2 | 15000
Siti Aminah | Bandung | 2026-10-01 | 1 | 1250000
Andi Wijaya | Surabaya | 2026-10-02 | 3 | 2500000
Dewi Lestari | Medan | 2026-10-03 |  | 75000
```

**Tips:** urutan langkahnya penting. Huruf diseragamkan **sebelum** duplikat dicari, supaya `JAKARTA` dan `Jakarta` dianggap sama. Hasilnya bisa langsung dianalisis dengan [analisis_csv.py](#11-analisis_csvpy).

**Batasan:**
- Koma dianggap pemisah desimal, dan titik dengan tepat tiga digit setelahnya dianggap pemisah ribuan (`1.500` dibaca seribu lima ratus).
- `.title()` tidak mengenal singkatan (`PT` menjadi `Pt`), jadi pilih kolom huruf dengan hati-hati.
- Duplikat berarti baris yang sama persis di semua kolom.

---

## 13. Laporan excel.py

**Fungsi:** mengubah file CSV menjadi **laporan Excel (`.xlsx`)** yang rapi, lengkap dengan ringkasan dan grafik. **File CSV asli tidak diubah.** Kamu tidak perlu membuat Excel dulu: inputnya CSV, file Excel dibuat oleh programnya.

Isi file Excel yang dihasilkan:
- **Sheet Ringkasan:** jumlah baris dan kolom, statistik tiap kolom angka (total, rata-rata, minimum, maksimum), total per kelompok beserta persennya, dan grafik batang
- **Sheet Data:** data asli dengan header berwarna, lebar kolom otomatis, baris header terkunci, dan filter

Semua angka di sheet Ringkasan berupa **rumus Excel** (`SUM`, `AVERAGE`, `SUMIF`), jadi kalau data di sheet Data diedit, ringkasan dan grafik ikut berubah.

**Persiapan:** pasang library `openpyxl` satu kali saja:

```
pip install openpyxl
```

**Cara pakai:**
1. Siapkan file CSV, misalnya `penjualan.csv` dari [proyek 11](#11-analisis_csvpy) atau hasil [bersihkan_csv.py](#12-bersihkan_csvpy).
2. Jalankan programnya, lalu masukkan lokasi lengkap file CSV.
3. Pilih nomor kolom teks untuk dikelompokkan (misalnya `kategori`).
4. Pilih nomor kolom angka yang dijumlahkan (misalnya `jumlah`).
5. Laporan tersimpan di folder yang sama dengan CSV, dengan nama `namafile_laporan.xlsx`.

**Contoh (pakai `penjualan.csv`, kelompok `kategori`, jumlahkan `jumlah`):**

```
=== PEMBUAT LAPORAN EXCEL ===
Lokasi file CSV: C:\Users\HP\penjualan.csv

Kolom teks (untuk dikelompokkan):
  1. tanggal
  2. produk
  3. kategori
Pilih nomor kolom kelompok: 3

Kolom angka (untuk dijumlahkan):
  1. jumlah
  2. harga
Pilih nomor kolom yang dijumlahkan: 1

Laporan tersimpan: C:\Users\HP\penjualan_laporan.xlsx
Isi: sheet Ringkasan (6 baris data) dan sheet Data.
```

Isi sheet Ringkasan:

```
Jumlah baris data   6
Jumlah kolom        5

Kolom     Total     Rata-rata    Minimum   Maksimum
jumlah    56        9.33         5         15
harga     89,000    14,833.33    8,000     22,000

Total jumlah per kategori
kategori   Total   Persen
Minuman    45      80.4%
Makanan    11      19.6%
Total      56
```

**Tips:** urutan alurnya: [bersihkan_csv.py](#12-bersihkan_csvpy) (membersihkan), lalu `Laporan excel.py` (membuat laporan Excel). Kolom angka berformat `Rp 15.000` tidak terbaca sebagai angka, jadi bersihkan dulu.

**Batasan:**
- Kolom angka hanya dikenali kalau semua isinya angka standar (tanpa `Rp` dan titik ribuan).
- Total per kelompok hanya untuk satu kolom angka dalam satu kali jalan.
- Kalau file `.xlsx` sedang terbuka di Excel, tutup dulu sebelum menjalankan ulang.

---

## Catatan keamanan

- Jangan mengunggah password atau data pribadi ke repo ini.
- File data hasil program (seperti `kontak.json` dan `keuangan.json`) berisi data pribadi dan sebaiknya tidak ikut diunggah.
