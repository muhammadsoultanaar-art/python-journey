barang = []
total = 0
lanjut = "y"

while lanjut == "y":
    nama = input("nama barang: ")
    harga = int(input("harga: "))
    jumlah = int(input("jumlah: "))
    subtotal = harga * jumlah
    barang.append((nama, jumlah, subtotal))
    total = total + subtotal
    lanjut = input("tambah barang lagi? (y/n): ")

if total >= 100000:
    diskon = 0.2
elif total >= 50000:
    diskon = 0.1
else:
    diskon = 0

bayar = total * (1-diskon)

print("=" * 30)
print(f"{'STRUK':^30}")
print("=" * 30)
for nama, jumlah, subtotal in barang:
    print(f"{nama:<14}{jumlah:>4}{subtotal:>12,}")
print("=" * 30)
print(f"{'total':<18}{total:>12,}")
print(f"{'diskon':<18}{diskon:>12.0%}")
print(f"{'bayar':<18}{bayar:>12,.0f}")
print("=" * 30)


