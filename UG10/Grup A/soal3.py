soal1 = int(input("Masukkan nilai soal 1: "))
soal2 = int(input("Masukkan nilai soal 2: "))
soal3 = int(input("Masukkan nilai soal 3: "))
umur = int(input("Masukkan umur anda: "))

#rumus nilai
nilai1 = (soal1*50/100)
nilai2 = (soal2*30/100)
nilai3 = (soal3*20/100)
rata = (nilai1 + nilai2 + nilai3)

#output nilai
print("Rata-rata nilai Anda: ", rata)

#rumus kriteria
if rata >= 80 and umur <= 25:
    print("Selamat Anda lulus!")
elif rata >= 90 and umur >= 25:
    print("Selamat Anda lulus!")
else:
    print("Coba lagi tahun depan")