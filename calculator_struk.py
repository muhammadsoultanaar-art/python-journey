harga = int(input("harga: "))
jumlah = int(input("jumlah: "))
total = harga * jumlah
if total >= 100000:
    diskon = 0.1
else:
    diskon = 0
total_akhir = total * (1 - diskon)
print("=" * 23)
print(f"{'STRUK':^23}")
print("=" * 23)
print(f"{'harga' :<8} {harga:>12,}")
print(f"{'jumlah' :<8} {jumlah:>12,}")
print(f"{'total' :<8} {total:>12,}")
print(f"{'diskon' :<8} {diskon:>12.0%}")
print(f"{'bayar' :<8} {total_akhir:>12,.0f}")
print('=' * 23)
