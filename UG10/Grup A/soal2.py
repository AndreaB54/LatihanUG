print("="*5, "Selamat datang di Toko Andi Tersenyum, selamat belanja!", "="*5)
total = int(input("Total belanja : Rp."))

#rumus
if total < 100000:
    print("Tidak ada diskon! Maka yang Anda bayarkan adalah: Rp.", total)
elif total >= 1000000:
    diskon3 = (total-(total*(0.1)))
    print("Biaya yang harus dibayar setelah diskon adalah: Rp.", diskon3)
elif total >= 500000:
    diskon2 = (total-(total*(0.05)))
    print("Biaya yang harus dibayar setelah diskon adalah: Rp.", diskon2)
elif total >= 100000:
    diskon1 = (total-(total*(0.02)))
    print("Biaya yang harus dibayar setelah diskon adalah: Rp.", diskon1)


