#Soal Hal 48 Nomor 20

nama_tim = input("Masukkan nama tim baseball: ")
menang = int(input("Masukkan jumlah pertandingan yang dimenangkan: "))
kalah = int(input("Masukkan jumlah pertandingan yang kalah: "))

persentase_menang = (menang / (menang + kalah)) * 100

print(nama_tim, persentase_menang)