ALFABET = "abcdefghijklmnopqrstuvwxyz"

def bersihkan_teks(teks):
    hasil = ""

    for karakter in teks:
        karakter_kecil = karakter.lower()

        if karakter_kecil in ALFABET:
            hasil += karakter_kecil

    return hasil

def cek_palinrome(teks):
    teks_balik = "".join(reversed(teks)) 

    if teks == teks_balik:
        return (True, -1)

    for i in range(len(teks)):
        if teks[i] != teks_balik[i]:
            return (False, i)

    return (True, -1)

def inti_palinrome(teks):
    teks_bersih = bersihkan_teks(teks)
    if teks_bersih == "":
        return {
            "teks": "",
            "panjang": 0,
            "indeks_awal": -1
        }
    palindrom_terbaik = ""
    indeks_terbaik = 0
    
    for i in range(len(teks_bersih)):
        for j in range(i + 1, len(teks_bersih) + 1):
            bagian = teks_bersih[i:j]

            hasil_cek = cek_palinrome(bagian)

            if hasil_cek[0]:
                if len(bagian) > len(palindrom_terbaik):
                    palindrom_terbaik = bagian
                    indeks_terbaik = i

    return {
        "teks": palindrom_terbaik,
        "panjang": len(palindrom_terbaik),
        "indeks_awal": indeks_terbaik
    }

teks = input("masukkan teks prasasti: ")

hasil = inti_palinrome(teks)

print("teks bersih :", bersihkan_teks(teks))
print("hasil       :", hasil)