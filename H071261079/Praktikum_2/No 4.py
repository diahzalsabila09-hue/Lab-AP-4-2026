# 4. Rekomendasi Wisata

tujuan = input("Masukkan tujuan (Pantai/Pegunungan/Kota): ").capitalize()
if tujuan not in ["Pantai", "Pegunungan", "Kota"]:
    print("Tujuan tidak valid.")
else:
    waktu = input("Masukkan waktu (Pagi/Malam): ").capitalize()
    if waktu not in ["Pagi", "Malam"]:
        print("Waktu tidak valid.")
    else:
        tipe = input("Masukkan tipe pengunjung (Anak/Dewasa): ").capitalize()
        if tipe not in ["Anak", "Dewasa"]:
            print("Tipe pengunjung tidak valid.")
        else:
            match tujuan:
                case "Pantai":
                    if waktu == "Pagi" and tipe == "Dewasa":
                        print("Paket Rekomendasi: Paket C")
                    elif waktu == "Pagi":
                        print("Paket Rekomendasi: Paket A")
                    else:
                        print("Tidak ada paket yang cocok")

                case "Pegunungan":
                    if waktu == "Pagi" and tipe == "Dewasa":
                        print("Paket Rekomendasi: Paket B")
                    elif waktu == "Malam" and tipe == "Dewasa":
                        print("Paket Rekomendasi: Paket C")
                    else:
                        print("Tidak ada paket yang cocok")

                case "Kota":
                    if waktu == "Malam":
                        print("Paket Rekomendasi: Paket C")
                    else:
                        print("Tidak ada paket yang cocok")

                case _:
                    print("Tidak ada paket yang cocok")