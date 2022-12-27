print("="*10, "Pilih Menu", "="*10)
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")
nilai1 = int(input("Masukkan angka pertama: "))
nilai2 = int(input("Masukkan angka kedua: "))
pilih = input("Pilihan Anda: ")

#rumus
if pilih == "1":
    tambah = (nilai1 + nilai2)
    print ("hasil:", tambah)

elif pilih == "2":
    kurang = (nilai1 - nilai2)
    print ("hasil:", kurang)

elif pilih == "3":
    kali = (nilai1 * nilai2)
    print ("hasil:", kali)

elif pilih == "4":
    bagi = (nilai1 / nilai2)
    print ("hasil:", bagi)