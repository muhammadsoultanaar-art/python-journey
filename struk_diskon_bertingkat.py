total = 0
lanjut = "y"

while lanjut == "y":
    harga = int(input("harga: "))
    jumlah = int(input("jumlah: "))
    total = total + harga * jumlah
    lanjut = input("tambah barang lagi? (y/n): ")

if total >= 100000:
    diskon = 0.2
elif total >= 50000:
    diskon = 0.1
else:
    diskon = 0

total_akhir = total * (1 - diskon)
print("=" * 23)
print(f"{'STRUK':^23}")
print("=" * 23)
print(f"{'Total':<8} : {total:>12,}")
print(F"{'Diskon':<8} : {diskon:>12.0%}")
print(F"{'Bayar':<8} : {total_akhir:>12,.0f}")
print("=" * 23)


