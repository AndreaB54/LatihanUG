nama=str(input("Masukkan nama Anda : "))
matakuliah=str(input("Masukkan mata kuliah : "))
grup=str(input("Masukkan grup : "))

print("Haloo!", nama.split()[-1] + ',', nama.replace(nama.split()[-1],''))
print(nama.split()[0], "tergabung dalam kelas", matakuliah, "pada grup", grup)