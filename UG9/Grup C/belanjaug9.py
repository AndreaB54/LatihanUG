print("========== CATATAN BELANJA ==========")
print("========== Daftar 1 ==========")
print("Daftar Belanja 1: ['Sikat Gigi', 'Odol', 'Shampoo', 'Sabun', 'Ciduk']")
print("")
print("========== Daftar 2 ==========")
print("Daftar Belanja 2: ['Teh', 'Gula', 'Garam', 'Micin', 'Kecap']")
print("")
print("Jawab dengan angka [1/2]")
print("1. Rubah Belanjaan")
print("2. Keluar")
pilihan=int(input("Masukkan Pilihan: "))
item1=str(input("Masukkan nama item ke daftar 1: "))
index1=int(input("Masukkan index yang ingin dirubah: "))
item2=str(input("Masukkan nama item ke daftar 2: "))
index2=int(input("Masukkan index yang ingin dirubah: "))
print("")

#data
data1=['Sikat Gigi', 'Odol', 'Shampoo', 'Sabun', 'Ciduk']
data2=['Teh', 'Gula', 'Garam', 'Micin', 'Kecap']

#input
if pilihan == 1 :
    data1[index1] = item1
    data2[index2] = item2
    print("========== Daftar 1 ==========")
    print("Daftar Belanja 1 : ", data1)
    print("")
    print("========== Daftar 2 ==========")
    print("Daftar Belanja 2 : ", data2)

elif pilihan == 2 :
    print("========== Daftar 1 ==========")
    print("Daftar Belanja 1 : ", data1)
    print("")
    print("========== Daftar 2 ==========")
    print("Daftar Belanja 2 : ", data2)

else:
    print("WRONG INPUT")