#Soal Hal 57 Nomor 4

hargaAsli = 150000
#Diskon dalam bentuk persen Misal 10%
Diskon = 10

PotonganHarga = hargaAsli * ( Diskon / 100 )

HargaSetelahDiskon = hargaAsli - PotonganHarga

print(f"Harga Asli = Rp. {hargaAsli:,}".replace(",", "."))
print(f"Diskon = {Diskon}%")
print(f"Harga setelah diskon = Rp. {int(HargaSetelahDiskon):,}".replace(",", "."))

#Fungsi Dari replace(",", ".")) Adalah mengganti 150,000 jadi 150.000