#pake dictionary
bulan = {
    "bulan31" : [1, 3, 5, 7, 8, 10, 12],
    "bulan30" : [4, 6, 9, 11],
    "bulan28" : [2]
}

#input
pilih = int(input("Masukkan bulan (1-12): "))

#rumus
if pilih in bulan["bulan31"]:
    print("Jumlah Hari : 31")

elif pilih in bulan["bulan30"]:
    print("Jumlah Hari : 30")

elif pilih in bulan["bulan28"]:
    print("Jumlah Hari : 28")

else:
    print("1 Tahun hanya punya 12 bulan\nJalankan ulang program")