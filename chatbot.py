def hitung_diskon(total):
    if total >= 100000:
        return 0.2
    elif total >= 50000:
        return 0.1
    else:
        return 0

def jawab(pesan):
    pesan = pesan.lower()
    if "halo" in pesan:
        return"halo! ada yang bisa dibantu?"
    elif "diskon" in pesan:
        total = int(input("total belanja: "))
        d = hitung_diskon(total)
        return f"diskon kamu {d:.0%}"
    elif "bye" in pesan:
        return "sampai jumpa!"
    else:
        return "maaf,aku belum paham."

while True:
    pesan = input("kamu: ")
    if pesan == "keluar":
        break
    print("bot=", jawab(pesan))