pesanan = str(input("Masukkan daftar pesanan : "))
daftar = pesanan.title()
print("Daftar pesanan: ", daftar.split(","))
tambahan = str(input("Masukkan pesanan yang ingin ditambahkan : "))

#rumus
if tambahan in pesanan :
    print(tambahan.upper(), "sudah berada dalam daftar pesanan.")
else:
    daftarbaru = pesanan.title(), tambahan.title()
    print("Hasil penambahan pada daftar pesanan : ", daftarbaru)