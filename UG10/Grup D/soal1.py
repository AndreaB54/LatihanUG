print("\(^o^) Selamat datang di Kalkulator Sederhana (^c^)/")
print("Ketik 1 untuk menghitung penjumlahan.\nKetik 2 untuk menghitung pengurangan.\nKetik 3 untuk menghitung perkalian\nKetik 4 untuk menghitung pembagian.\nKetik 5 untuk menghitung sisa hasil bagi(modulus).\nKetik 6 untuk menghitung pemangkatan.")
pilih = int(input("Masukkan pilihan Anda: "))
bil1 = int(input("Masukkan bilangan pertama: "))
bil2 = int(input("Masukkan bilangan kedua: "))

#rumus
if pilih == 1 :
    tambah = bil1 + bil2
    print ("Hasil dari", bil1, "dijumlahkan dengan", bil2, "adalah", tambah)
elif pilih == 2 :
    kurang = bil1 - bil2
    print ("Hasil dari", bil1, "dikurangkan dengan", bil2, "adalah", kurang)
elif pilih == 3 :
    kali = bil1 * bil2
    print ("Hasil dari", bil1, "dikalikan dengan", bil2, "adalah", kali)
elif pilih == 4 :
    bagi = bil1 / bil2
    print ("Hasil dari", bil1, "dibagi dengan", bil2, "adalah", bagi)
elif pilih == 5 :
    modulus = bil1 % bil2
    print ("Hasil dari", bil1, "dimodulus dengan", bil2, "adalah", modulus)
elif pilih == 6 :
    pangkat = bil1 ** bil2
    print ("Hasil dari", bil1, "dipangkatkan dengan", bil2, "adalah", pangkat)