kecepatan=int(input("Masukkan kecepatan tempuh : "))
waktu=int(input("Masukkan waktu yang diperlukan : "))

bbm=int(kecepatan*waktu/10)
harga=int(bbm*15000)

print("Teman Anda mengisi bensin sebanyak", bbm, "liter")
print("Biaya yang dikeluarkan untuk mengisi bensin adalah Rp.", harga)