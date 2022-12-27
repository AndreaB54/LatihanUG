tahun = int(input("Masukkan Tahun: "))

#rumus
if tahun % 4 or tahun % 400== 0:
    print(tahun, "merupakan Tahun Kasbiat.")
else:
    print(tahun, "bukan merupakan Tahun Kasbiat.")