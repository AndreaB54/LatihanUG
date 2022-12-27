nama = str(input("Masukkan nama mahasiswa : "))
nim = str(input("Masukkan NIM-nya : "))
angkatan = int(nim[2:4])
prodi = int(nim[0:2])
#rumus
if prodi == 71:
    if angkatan >= 20 and angkatan <= 22 :
        print (nama, "merupakan mahasiswa informatika angkatan 20 hingga 22")
    else :
        print(nama, "bukan mahasiswa informatika angkatan 20 hingga 22")
else :
    print(nama, "bukan mahasiswa informatika")