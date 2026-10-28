import random
rahasia = random.randint(1,100)
tebakan = 0
percobaan = 0

while tebakan != rahasia:
    tebakan = int(input("tebak angka (1-100): "))
    percobaan = percobaan + 1
    if tebakan < rahasia:
        print("terlalu  kecil")
    if tebakan > rahasia:
        print("terlalu  besar")

print(f"benar! kamu butuh {percobaan} percobaan")