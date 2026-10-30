import math

AMAN = {"__builtins__": {}, "abs": abs, "sqrt": math.sqrt}


def hitung(rumus, x):
    try:
        return eval(rumus, AMAN, {"x": x})
    except Exception:
        return None


def tampil(nilai):
    if nilai is None:
        return "tidak terdefinisi"
    return round(nilai, 4)


def sama(nilai, target):
    return nilai is not None and abs(nilai - target) < 0.0001


def baca_angka(pesan):
    try:
        return float(input(pesan))
    except ValueError:
        return None


def tabel():
    rumus = input("f(x) = ")
    awal = baca_angka("x awal: ")
    akhir = baca_angka("x akhir: ")
    if awal is None or akhir is None:
        print("Harus angka")
        return
    print("=" * 26)
    print(f"{'x':>6}{'f(x)':>20}")
    for x in range(int(awal), int(akhir) + 1):
        print(f"{x:>6}{tampil(hitung(rumus, x)):>20}")
    print("=" * 26)


def komposisi():
    f = input("f(x) = ")
    g = input("g(x) = ")
    x = baca_angka("x = ")
    if x is None:
        print("Harus angka")
        return
    fg = hitung(f, hitung(g, x))
    gf = hitung(g, hitung(f, x))
    print(f"(f o g)({x}) = {tampil(fg)}")
    print(f"(g o f)({x}) = {tampil(gf)}")


def cek_pertidaksamaan():
    syarat = input("Pertidaksamaan, contoh abs(x-2) < 3: ")
    cocok = []
    for x in range(-20, 21):
        if hitung(syarat, x):
            cocok.append(x)
    if len(cocok) == 0:
        print("Tidak ada bilangan bulat -20..20 yang memenuhi")
    else:
        print("Bilangan bulat -20..20 yang memenuhi:", cocok)


def cek_invers():
    f = input("f(x) = ")
    g = input("Tebakan invers g(x) = ")
    lolos = True
    for x in [1, 2, 3, 5, 10]:
        a = hitung(f, hitung(g, x))
        b = hitung(g, hitung(f, x))
        if not sama(a, x) or not sama(b, x):
            lolos = False
            print(f"x = {x}: f(g(x)) = {tampil(a)}, g(f(x)) = {tampil(b)}")
    if lolos:
        print("Cocok di semua titik uji, kemungkinan benar invers")
    else:
        print("Belum cocok")


while True:
    print("1. Tabel f(x)  2. Komposisi  3. Pertidaksamaan  4. Cek invers  0. Keluar")
    menu = input("Pilih menu: ")
    if menu == "1":
        tabel()
    elif menu == "2":
        komposisi()
    elif menu == "3":
        cek_pertidaksamaan()
    elif menu == "4":
        cek_invers()
    elif menu == "0":
        break
    else:
        print("Menu tidak ada")

print("Sampai jumpa")