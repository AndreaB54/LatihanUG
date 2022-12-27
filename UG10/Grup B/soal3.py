print ("~~ Selamat Datang di Program Pengurutan Bilangan ~~\nTentukan Pilihan Anda!!! [1/2]\n")
print("1. Ascending\n2. Descending\n\n")
pilih = int(input("Masukkan Pilihan yang Anda Inginkan: "))
print("")

bil1 = int(input("Masukkan bilangan pertama : "))
bil2 = int(input("Masukkan bilangan kedua : "))
bil3 = int(input("Masukkan bilangan ketiga : "))
bil4 = int(input("Masukkan bilangan keempat : "))
data = bil1, bil2, bil3, bil4

if pilih == 1:
    print ("Urutan bilangan dari yang terkecil adalah", sorted(data))
elif pilih == 2 :
    print ("Urutan bilangan dari yang terbesar adalah", sorted(data, reverse=True))
