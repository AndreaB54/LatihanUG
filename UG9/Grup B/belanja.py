print("="*10, "CATATAN BELANJA", "="*10)
print("="*10, "Daftar 1", "="*10)
print("Daftar Belanja 1: ['Sikat Gigi', 'Odol', 'Shampoo', 'Sabun', 'Ciduk']")
print("")
print("="*10, "Daftar 2", "="*10)
print("Daftar Belanja 2: ['Teh', 'Gula', 'Garam', 'Micin', 'Kecap']")

#data
belanja1 = ['Sikat Gigi', 'Odol', 'Shampoo', 'Sabun', 'Ciduk']
belanja2 = ['Teh', 'Gula', 'Garam', 'Micin', 'Kecap']
print("")

#input
print("Jawab dengan angka [1/2]")
print("1. Rubah Belanjaan")
print("2. Keluar")
pilih = int(input("Masukkan Pilihan: "))
daftar1 = str(input("Masukkan nama item ke daftar 1: "))
index1 = int(input("Masukkan index yang ingin dirubah: "))
daftar2 = str(input("Masukkan nama item ke daftar 2: "))
index2 = int(input("Masukkan index yang ingin dirubah: "))
print("")

#rumus
if pilih == 1 :
    belanja1[index1] = daftar1
    belanja2[index2] = daftar2
    print("="*10, "Daftar 1", "="*10)
    print("Daftar Belanja 1: ", belanja1)
    print("")
    print("="*10, "Daftar 2", "="*10)
    print("Daftar Belanja 2: ", belanja2)

elif pilih == 2 :
    print("="*10, "Daftar 1", "="*10)
    print("Daftar Belanja 1: ", belanja1)
    print("")
    print("="*10, "Daftar 2", "="*10)
    print("Daftar Belanja 2: ", belanja2)

else:
    print ("WRONG INPUT")