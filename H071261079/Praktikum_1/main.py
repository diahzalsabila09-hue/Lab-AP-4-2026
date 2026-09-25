menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]
BIAYA_OPERASIONAL =15000

#Hitung Subtotal
sub_kopi = harga[0]*jumlah[0]
sub_matcha = harga[1]*jumlah[1]
sub_americano = harga[2]*jumlah[2]

#Subtotal Pendapatan
subtotal_pendapatan = [ sub_kopi, sub_matcha, sub_americano]

#Total
total_seluruh = sum(subtotal_pendapatan)
pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL

#total barang terjual
jumlah_barang = (jumlah)
target_tercapai = total_seluruh > 200000 and jumlah_barang > 10

print(" Subtotal          : Rp", total_seluruh )
print(" Pendapatan Bersih : Rp", pendapatan_bersih)
print(" Hasil Target      : ", target_tercapai)
